let lux = 0 
basic.forever(function () {
    lux = input.lightLevel()

        if (lux > 20) {
            basic.showString("day")
        } else if (lux < 20) {
            basic.showString("night")
        }
})
