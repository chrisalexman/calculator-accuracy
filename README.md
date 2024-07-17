# TI-36X Pro Calculator Accuracy

Calculating the accuracy of the TI-36X Pro calculator using Taylor & Maclaurin series expansions.

NOTE: constraint, calculator can represent max of 9 digits to the right of the decimal

Functions to test:
- exponential (e^x)
- trigonometric (sin x)

https://en.wikipedia.org/wiki/Taylor_series

## Result

| Function | terms needed | result |
| :--- | :--- | :---  |
| exponential | 17 | 7.389056099 |
| sine | 9 | 0.909297427 |

The trigonometric function (sine) needed nearly half the number of polynomial terms to sum to arrive at its respective approximation. This is possibly due to calculators like the TI-36X Pro not using Taylor or Maclaurin series for trigonometric functions but instead the CORDIC algorithm ([source](https://math.stackexchange.com/questions/395600/how-does-a-calculator-calculate-the-sine-cosine-tangent-using-just-a-number), [wiki](https://en.wikipedia.org/wiki/CORDIC)).
