from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        df_data_1 = X.copy()

        coluna  = df_data_1['NOTA_DE']
        coluna1 = df_data_1['NOTA_EM']
        coluna2 = df_data_1['NOTA_MF']
        coluna3 = df_data_1['NOTA_GO']
        coluna4 = df_data_1['PERFIL']

        for i in range(df_data_1['NOTA_DE'].shape[0]) :
            if((math.isnan(coluna[i]))):
                coluna[i] = coluna1[i]
            if((math.isnan(coluna1[i]))):
                coluna1[i] = coluna[i]
            if((math.isnan(coluna2[i]))):
                 coluna2[i] = coluna3[i]
            if((math.isnan(coluna3[i]))):
                 coluna3[i] = coluna2[i]

#       valida se a nota foi muito boa
        var1 = (coluna[i] + coluna1[i] >= 12) & (coluna[i] + coluna1[i] < 16)
        var2 = (coluna2[i] + coluna3[i] >= 12) & (coluna2[i] + coluna3[i] < 16)
    
#       valida se a nota foi exelente
        var3 = coluna[i] + coluna1[i] >= 16
        var4 = coluna2[i] + coluna3[i] >= 16
     
#       atribui o sufixo equivalente ao nv da nota de humanas
        if any((var1 , var3)):
            if(var1):
                 v1 = 'mb'
            else:
                v1 = 'ex'
        else:
            v1 = 'mal'
        
#       atribui o sufixo equivalente ao nv da nota de exatas
        if any((var2 , var4)):
            if(var2):
                v2 = 'mb'
            else:
                v2 = 'ex'
        else:
            v2 = 'mal'
        
        v = v1+v2
    
#       atribui o a clasificacao geral do aluno
        if(v=='exex'):
            res='EXCELENTE'
        if(v=='mbmb' or v=='mbex' or v=='exmb'):
            res='MUITO_BOM'
        if(v=='malmal'):
            res='DIFICUDADE'
        if(v=='mbmal' or v=='exmal'):
            res='EXATA'
        if(v=='malmb' or v=='malex'):
            res='HUMANAS'
    
        coluna4[i]=res

#       atualiza o data set
        df_data_1 = coluna
        df_data_1 = coluna1
        df_data_1 = coluna2
        df_data_1 = coluna3
        df_data_1 = coluna4
        
        # Primeiro realizamos a cópia do dataframe 'X' de entrada mas antes consertamos possiveis ruidos
        data = df_data_1
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
