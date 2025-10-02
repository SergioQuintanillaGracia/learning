const numbers = [1, 2, 3, 4]
const doubled = numbers.map((num) => num * 2)
console.log(doubled)

// These are objects
const users = [
    {name: "Alice", age: 25},
    {name: "Bob", age: 30}
]

const names = users.map((user) => user.name)
console.log(names)

// Reduce is used to reduce an array to a single value
// acc is the accumulator, its value is conserved during the execution of reduce
// 0 is the value the accumulator starts at
const nums = [1, 2, 3, 4]
const sum = nums.reduce((acc, num) => acc + num, 0)
console.log(sum)

const numbers3 = [1, 2, 3, 4, 5]
const evenNumbers = numbers3.filter(num => num % 2 === 0)
console.log(evenNumbers)