function greet(name, age=12) {
    console.log("Hi",name, "with age", age)
}

const greet1 = function(name) {
    console.log("Whatever")
}

const greet2 = (name) => name + "!"

const greet3 = (name) => {
    return () => name  // This makes no sense, it's just an example
}


function addNums(...numbers) {
    let sum = 0
    for (const val of numbers) {
        sum += val
    }
    return sum
}

console.log(addNums(1, 2, 3, 4))