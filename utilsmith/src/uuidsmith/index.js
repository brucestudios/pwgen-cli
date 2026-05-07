/**
 * UUID Smith - A comprehensive UUID/GUID utility toolkit
 * @module uuidsmith
 */

const crypto = require('crypto');

/**
 * Generate a random UUID (version 4)
 * @returns {string} UUID string in the format xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx
 */
function generateV4() {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    const r = crypto.randomBytes(1)[0] % 16 | 0;
    const v = c === 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
  });
}

/**
 * Generate a UUID (version 1) based on timestamp and node ID
 * @returns {string} UUID string in the format xxxxxxxx-xxxx-1xxx-yxxx-xxxxxxxxxxxx
 */
function generateV1() {
  const now = Date.now();
  const timestamp = now * 10000 + 0x01b21dd213814000; // Convert to 100-ns intervals since 1582-10-15
  const timestampLow = timestamp & 0xffffffff;
  const timestampMid = (timestamp >> 32) & 0xffff;
  const timestampHiAndVersion = ((timestamp >> 48) & 0x0fff) | 0x1000; // Version 1

  // Generate a random node ID (48 bits)
  const node = crypto.randomBytes(6);
  const clockSeqHiAndReserved = crypto.randomBytes(1)[0] & 0x3f | 0x80; // Set variant to 10
  const clockSeqLow = crypto.randomBytes(1)[0];

  return (
    padHex(timestampLow, 8) + '-' +
    padHex(timestampMid, 4) + '-' +
    padHex(timestampHiAndVersion, 4) + '-' +
    padHex(clockSeqHiAndReserved, 2) + padHex(clockSeqLow, 2) + '-' +
    node.toString('hex')
  );
}

/**
 * Validate a UUID string (versions 1, 2, 3, 4, 5)
 * @param {string} uuid - UUID string to validate
 * @returns {boolean} True if valid, false otherwise
 */
function validate(uuid) {
  const uuidPattern = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
  return uuidPattern.test(uuid);
}

/**
 * Get the version of a UUID string
 * @param {string} uuid - UUID string
 * @returns {number|null} Version number (1-5) or null if invalid
 */
function getVersion(uuid) {
  if (!validate(uuid)) return null;
  return parseInt(uuid.charAt(14), 16);
}

/**
 * Format a UUID string (uppercase, lowercase, etc.)
 * @param {string} uuid - UUID string to format
 * @param {Object} options - Formatting options
 * @param {boolean} [options.uppercase=false] - Convert to uppercase
 * @param {boolean} [options.lowercase=false] - Convert to lowercase (default)
 * @param {boolean} [options.urn=false] - Prefix with 'urn:uuid:'
 * @returns {string} Formatted UUID
 */
function format(uuid, options = {}) {
  if (!validate(uuid)) throw new Error('Invalid UUID string');
  let formatted = uuid;
  if (options.uppercase) formatted = formatted.toUpperCase();
  else if (options.lowercase) formatted = formatted.toLowerCase();
  if (options.urn) formatted = `urn:uuid:${formatted}`;
  return formatted;
}

/**
 * Generate a UUID of specified version
 * @param {number} version - UUID version (1 or 4)
 * @returns {string} UUID string
 */
function generate(version = 4) {
  switch (version) {
    case 1: return generateV1();
    case 4: return generateV4();
    default: throw new Error('Only UUID versions 1 and 4 are supported');
  }
}

function padHex(number, length) {
  let hex = number.toString(16);
  while (hex.length < length) hex = '0' + hex;
  return hex;
}

module.exports = {
  generate,
  generateV1,
  generateV4,
  validate,
  getVersion,
  format
};