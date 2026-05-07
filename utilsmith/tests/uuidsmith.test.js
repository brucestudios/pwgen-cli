const { generate, generateV1, generateV4, validate, getVersion, format } = require('../src/uuidsmith/index');

describe('UUID Smith', () => {
  test('generateV4 produces a valid UUID v4', () => {
    const uuid = generateV4();
    expect(validate(uuid)).toBe(true);
    expect(getVersion(uuid)).toBe(4);
  });

  test('generateV1 produces a valid UUID v1', () => {
    const uuid = generateV1();
    expect(validate(uuid)).toBe(true);
    expect(getVersion(uuid)).toBe(1);
  });

  test('generate function works for v1 and v4', () => {
    const uuid1 = generate(1);
    const uuid4 = generate(4);
    expect(getVersion(uuid1)).toBe(1);
    expect(getVersion(uuid4)).toBe(4);
  });

  test('validate function correctly validates UUIDs', () => {
    const validUuid = '123e4567-e89b-12d3-a456-426614174000';
    expect(validate(validUuid)).toBe(true);
    expect(validate('invalid')).toBe(false);
    expect(validate('123e4567-e89b-12d3-a456-42661417400')).toBe(false); // too short
    expect(validate('123e4567-e89b-12d3-a456-4266141740000')).toBe(false); // too long
    expect(validate('123e4567-e89b-12d3-a456-42661417400g')).toBe(false); // invalid char
  });

  test('getVersion returns correct version', () => {
    const uuidV1 = '00000000-0000-1000-8000-000000000000'; // version 1
    const uuidV4 = '00000000-0000-4000-8000-000000000000'; // version 4
    expect(getVersion(uuidV1)).toBe(1);
    expect(getVersion(uuidV4)).toBe(4);
  });

  test('format function works', () => {
    const uuid = '123e4567-e89b-12d3-a456-426614174000';
    expect(format(uuid, { uppercase: true })).toBe(uuid.toUpperCase());
    expect(format(uuid, { lowercase: true })).toBe(uuid.toLowerCase());
    expect(format(uuid, { urn: true })).toBe(`urn:uuid:${uuid}`);
    expect(format(uuid, { uppercase: true, urn: true })).toBe(`urn:uuid:${uuid.toUpperCase()}`);
  });

  test('format throws on invalid UUID', () => {
    expect(() => format('invalid', {})).toThrow('Invalid UUID string');
  });
});