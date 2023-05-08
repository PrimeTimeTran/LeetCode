function map<T, U>(arr: T[], fn: (value: T, index: number) => U): U[] {
  const mappedArray: U[] = [];
  for (let i = 0; i < arr.length; i++) {
    mappedArray.push(fn(arr[i], i));
  }
  return mappedArray;
}