const person = {
    name: "Alice",
    
    greet() {
        console.log(`Hello, my name is ${this.name}`)
    },

    greet2: function() {
        console.log(`Hello, my name is ${this.name}`)
    },

    // Using arrow functions, `this` searches in the global scope and not in the object,
    // so `this.name` is undefined
    greet3: () => {
        console.log(`Hello, my name is ${this.name}`)
    }
}

person.greet()
person.greet2()
person.greet3()