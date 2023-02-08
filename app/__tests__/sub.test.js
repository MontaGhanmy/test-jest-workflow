const sub = require('../feature2');

test('sub 2 - 1 to equal 1', () => {
  expect(sub(2, 1)).toBe(1);
});

// updated test
test('sub 2 - 2 to equal 0', () => {
  expect(sub(2, 2)).toBe(0);
});
