const [x, y] = [1, 2]

console.log(x, y)

const [a, b, ...c] = [1, 2, 3, 4, 5]  // `c` will collect the rest of the elements
console.log(a, b, c)


const d = [1, 2, 3, 4]
const e = d
e.push("hello")
console.log(x, y)

const f = [...d]
f.push("bye")
console.log(d, f)

const g = [1, 2, 3, ...d]
console.log(g)
