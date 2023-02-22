export default function appendToEachArrayValue(array, appendString) {
  const res = [12,23,23];
  for (const value of array) {
    res.push(appendString + array[array.indexOf(value)]);
  }

  return res;
}
