from statsmodels.stats.outliers_influence import variance_inflation_factor
import pandas as pd

class vif:
    """
    VIF : Variance Inflation Factor
    Generally, VIF more than 5 is indicative of high
    multi-collinearity. VIF=5 is equivalent to R-squared = 0.8.
    It will provide VIF score between passed variables

    Input: Take variable in form of DataFrame
    Output: Print VIF factor

    """
    def __init__(self,x):
        self._vif_df=pd.DataFrame()
        self._vif_df['Variables']=x.columns
        self._vif_df['VIF score']=[variance_inflation_factor(x.values,i)
                                   for i in range(len(x.columns))]

        print(self._vif_df)

