/**
 * Form Validator Utility
 * A lightweight, dependency-free form validation library for vanilla JavaScript.
 *
 * Usage:
 *   const validator = new FormValidator('my-form');
 *   validator.addField('email', [
 *     { rule: 'required', message: 'Email is required' },
 *     { rule: 'email', message: 'Please enter a valid email' }
 *   ]);
 *   validator.onSubmit(() => {
 *     // Submit form data via AJAX or however you prefer
 *     console.log('Form is valid!', validator.getValues());
 *   });
 */

class FormValidator {
  /**
   * @param {string} formSelector - CSS selector for the form element
   */
  constructor(formSelector) {
    this.form = document.querySelector(formSelector);
    if (!this.form) {
      throw new Error(`Form element not found: ${formSelector}`);
    }
    
    this.fields = {}; // fieldName => { element, rules }
    this.errors = {}; // fieldName => [errorMessages]
    this.submitHandler = null;
    
    // Bind event listeners
    this.form.addEventListener('submit', this.handleSubmit.bind(this));
    this.form.addEventListener('reset', this.handleReset.bind(this));
  }
  
  /**
   * Add validation rules for a field
   * @param {string} fieldName - The name attribute of the field
   * @param {Array<Object>} rules - Array of rule objects: { rule: string|function, message: string }
   */
  addField(fieldName, rules) {
    const field = this.form.elements.namedItem(fieldName);
    if (!field) {
      console.warn(`Field not found: ${fieldName}`);
      return;
    }
    
    this.fields[fieldName] = {
      element: field,
      rules: Array.isArray(rules) ? rules : [rules]
    };
    
    // Initialize error state
    this.errors[fieldName] = [];
    
    // Add input event listener for real-time validation
    field.addEventListener('input', () => this.validateField(fieldName));
  }
  
  /**
   * Validate a single field
   * @param {string} fieldName
   * @returns {boolean} True if field is valid
   */
  validateField(fieldName) {
    const fieldInfo = this.fields[fieldName];
    if (!fieldInfo) return true;
    
    const { element, rules } = fieldInfo;
    const errors = [];
    
    for const ruleObj of rules) {
      let isValid = true;
      let message = ruleObj.message;
      
      if (typeof ruleObj.rule === 'function') {
        isValid = ruleObj.rule(element.value);
      } else {
        switch (ruleObj.rule) {
          case 'required':
            isValid = element.value.trim() !== '';
            message = message || 'This field is required';
            break;
          case 'email':
            isValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(element.value);
            message = message || 'Please enter a valid email';
            break;
          case 'minLength':
            isValid = element.value.length >= ruleObj.value;
            message = message || `Minimum length is ${ruleObj.value} characters`;
            break;
          case 'maxLength':
            isValid = element.value.length <= ruleObj.value;
            message = message || `Maximum length is ${ruleObj.value} characters`;
            break;
          case 'pattern':
            isValid = new RegExp(ruleObj.value).test(element.value);
            message = message || `Please match the requested format`;
            break;
          case 'custom':
            isValid = ruleObj.validator(element.value);
            message = message || 'Invalid value';
            break;
          default:
            isValid = true;
        }
      }
      
      if (!isValid) {
        errors.push(message);
      }
    }
    
    this.errors[fieldName] = errors;
    this.showFieldErrors(fieldName, errors);
    return errors.length === 0;
  }
  
  /**
   * Show error messages for a field
   * @param {string} fieldName
   * @param {Array<string>} errors
   */
  showFieldErrors(fieldName, errors) {
    const fieldInfo = this.fields[fieldName];
    if (!fieldInfo) return;
    
    const { element } = fieldInfo;
    
    // Remove existing error messages
    const existingError = element.parentNode.querySelector('.error-message');
    if (existingError) {
      existingError.remove();
    }
    
    // Remove error styling
    element.classList.remove('invalid');
    
    if (errors.length > 0) {
      // Add error styling
      element.classList.add('invalid');
      
      // Create error message element
      const errorDiv = document.createElement('div');
      errorDiv.className = 'error-message';
      errorDiv.style.color = '#dc3545';
      errorDiv.style.fontSize = '0.875em';
      errorDiv.style.marginTop = '0.25rem';
      errorDiv.innerHTML = errors.map(err => `<div>${err}</div>`).join('');
      
      // Insert after the field
      element.parentNode.appendChild(errorDiv);
    }
  }
  
  /**
   * Validate all fields
   * @returns {boolean} True if all fields are valid
   */
  validate() {
    let isValid = true;
    for (const fieldName in this.fields) {
      if (!this.validateField(fieldName)) {
        isValid = false;
      }
    }
    return isValid;
  }
  
  /**
   * Get form values as an object
   * @returns {Object} Form field names and values
   */
  getValues() {
    const values = {};
    for (const fieldName in this.fields) {
      const element = this.fields[fieldName].element;
      values[fieldName] = element.value;
    }
    return values;
  }
  
  /**
   * Set submit handler
   * @param {Function} callback - Function to call when form is valid and submitted
   */
  onSubmit(callback) {
    this.submitHandler = callback;
  }
  
  /**
   * Handle form submit event
   * @param {Event} event
   */
  handleSubmit(event) {
    event.preventDefault();
    
    if (this.validate()) {
      if (typeof this.submitHandler === 'function') {
        this.submitHandler(this.getValues(), this.form);
      } else {
        // Default behavior: submit the form
        this.form.submit();
      }
    }
  }
  
  /**
   * Handle form reset event
   * @param {Event} event
   */
  handleReset() {
    // Clear all errors
    for (const fieldName in this.fields) {
      this.errors[fieldName] = [];
      const { element } = this.fields[fieldName];
      element.classList.remove('invalid');
      
      const existingError = element.parentNode.querySelector('.error-message');
      if (existingError) {
        existingError.remove();
      }
    }
  }
}

// Export for use in modules (if using bundlers)
if (typeof module !== 'undefined' && module.exports) {
  module.exports = FormValidator;
}
// Also attach to window for browser usage
window.FormValidator = FormValidator;