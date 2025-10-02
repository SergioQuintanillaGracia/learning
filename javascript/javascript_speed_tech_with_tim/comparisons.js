console.log("1" == 1)
console.log(true == 1)
console.log(true == undefined)
console.log(null == undefined)  // They are loosely equal to each other
console.log(null == false)
console.log(null == true)
console.log("" == 0)
console.log("" == [])
console.log("1,2" == [1, 2])
console.log("1, 2" == [1, 2])  // This is false

console.log(undefined === null)
console.log(undefined === "")
console.log(1 === "1")

console.log(2 < "3")
console.log("2" < "3")


console.log("hello" || true)  // "hello" is a truthy value, so it returns "hello" instead of true
console.log("" || true)
console.log("" || "hello")

console.log(true && "another")
console.log(false && "hi")

console.log(Boolean("hello") && Boolean(2))

const cond = 2 < 3 ? "ok" : "false"
console.log(cond)