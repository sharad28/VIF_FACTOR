

    VIF : Variance Inflation Factor
    Generally, VIF more than 5 is indicative of high
    multi-collinearity. VIF=5 is equivalent to R-squared = 0.8.
    It will provide VIF score between passed variables

    Input: Take variable in form of DataFrame
    Output: Print VIF factor

Variance Inflation Factor (VIF) Explained

Colinearity is the state where two variables are highly correlated and contain similiar information about the variance within a given dataset. To detect colinearity among variables, simply create a correlation matrix and find variables with large absolute values. In R use the corr function and in python this can by accomplished by using numpy's corrcoef function.

Multicolinearity on the other hand is more troublesome to detect because it emerges when three or more variables, which are highly correlated, are included within a model. To make matters worst multicolinearity can emerge even when isolated pairs of variables are not colinear.

A common R function used for testing regression assumptions and specifically multicolinearity is "VIF()" and unlike many statistical concepts, its formula is straightforward:

$$ V.I.F. = 1 / (1 - R^2). $$

The Variance Inflation Factor (VIF) is a measure of colinearity among predictor variables within a multiple regression. It is calculated by taking the the ratio of the variance of all a given model's betas divide by the variane of a single beta if it were fit alone.


reference:
https://etav.github.io/python/vif_factor_python.html