try {
    throw new Error("Something bad is going on")
} catch (error) {
    console.log("Error occurred:", error)
} finally {
    console.log("Always run")
}