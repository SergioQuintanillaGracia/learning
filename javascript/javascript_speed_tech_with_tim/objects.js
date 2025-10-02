const obj = {
    name: "Alice",
    age: 23,
    sayHello: function() {
        return "hello"
    },
    career: {}
}

obj.age = "asdf"
obj.newProp = [1, 2]

obj["name"] = "Juan"

console.log(obj)

delete obj.newProp
console.log(obj)

console.log(Object.values(obj))
console.log(Object.keys(obj))

for (let key in obj) {
    console.log(key)
}

const obj2 = {
    hairColor: "black",
    arr: [1, 2, 3],
    name: "Tim"
}

// Combine both objects
const obj3 = {...obj, ...obj2}
console.log(obj3)

obj3.career.info = "tech"
console.log(obj, obj3)  // `career` is modified in both objects

obj2.arr.push("hello")
console.log(obj2, obj3)  // Same, arr is modified in both

obj2.hairColor = "brown"
console.log(obj2, obj3)  // As `hairColor` is a primitive, it is not modified in obj3

const {hairColor, name} = obj3  // This grabs JUST these properties
console.log(hairColor, name)