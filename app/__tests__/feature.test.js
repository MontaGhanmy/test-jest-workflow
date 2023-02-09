const mul = require('../features/feature');

test('multiply 1 * 2 to equal 2', () => {
  expect(mul(1, 2)).toBe(2);
});

test('multiply 2 * 2 to equal 4', () => {
  expect(mul(2, 2)).toBe(4);
});
