const map = new Map()
const numberMap = new Map([[1, 'one'], [2, 'two']])

map.set(4, "four")
map.delete(4)
map.set(5, "five")
console.log(map.get(5))
console.log(map.has(5))
console.log(map.size)

for (const [key, value] of numberMap) {
    console.log(key, value)
}

for (const key of numberMap.keys()) {
    console.log(key)
}

for (const value of numberMap.values()) {
    console.log(value)
}

console.log(map)
map.clear()
console.log(map)

const arr = Array.from(numberMap)
console.log(arr)