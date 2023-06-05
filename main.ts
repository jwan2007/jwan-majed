input.onButtonPressed(Button.A, function () {
    basic.showNumber(8)
})
input.onGesture(Gesture.Shake, function () {
    basic.showArrow(ArrowNames.NorthEast)
})
basic.showIcon(IconNames.Heart)
basic.forever(function () {
    basic.showString("Jojo")
})
