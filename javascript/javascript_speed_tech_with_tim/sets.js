const set = new Set([1, 2, 3])
set.add(1)
set.add(5)
console.log(set)
set.delete(1)
console.log(set)
console.log(set.has(2))
console.log(set.size)

for (const val of set) {
    console.log(val)
}

set.clear()
console.log(set)
set.add(1)
set.add(4)

const arr = Array.from(set)
console.log(arr)

const arr2 = [...new Set([1, 2, 3])]
const arr3 = [...set]
console.log(arr2, arr3)