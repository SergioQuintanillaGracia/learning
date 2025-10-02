const arr = [1, 2, 3, true]
const arr2 = new Array(5)
console.log(arr2)
console.log(arr2[2])

const arr3 = Array.from("hello")
console.log(arr3)

arr2[0] = "y"
console.log(arr2)

console.log(arr3[arr3.length - 1])

arr3[arr3.length + 5] = "test"  // No error 💀
console.log(arr3)  // The array is expanded

arr3.push(4)
console.log(arr3)

console.log(arr3.pop())
console.log(arr3)

arr3.shift()  // Removes the first elements
console.log(arr3)

arr3.unshift("new")
console.log(arr3)

console.log(arr3.indexOf("o"))
console.log(arr3.lastIndexOf("l"))

console.log(arr3.includes("l"))

console.log(arr3.concat(arr))

const str = arr3.join("|")
console.log(str)

console.log(arr.slice(1, 3))

console.log(arr.splice(1, 2))  // Starting in index 1, remove 2 elements
console.log(arr)  // Now arr has lost those elements