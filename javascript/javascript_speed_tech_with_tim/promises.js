const myPromise = new Promise((resolve, reject) => {
    // Imagine this is an asynchronous operation
    if (true) {
        resolve("good")
    } else {
        reject("bad")
    }
})

myPromise.then((value) => {
    console.log(value)
}).catch((value) => {
    console.log(value)
}).finally(() => {
    console.log("Always runs")
})


const promise1 = Promise.resolve(3)
const promise2 = new Promise((resolve, reject) => setTimeout(resolve, 400, "foo"))
const promise3 = new Promise((resolve, reject) => setTimeout(reject, 700, "bar"))

Promise.all([promise1, promise2, promise3])
    .then((results) => {
        console.log(results)
    })
    .catch((error) => {
        console.log(error)
    })