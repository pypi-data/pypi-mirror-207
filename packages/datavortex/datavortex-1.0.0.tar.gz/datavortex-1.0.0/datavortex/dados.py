import pandas as pd
from pandas import DataFrame
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
from io import BytesIO
from PIL import Image
import io
import matplotlib.ticker as ticker
from loguru import logger
import json

class Analyzes:
    def __init__(self) -> None:
        """
        Classe responsável por conter os métodos de análise de dados.
        """
        self.__dpi = 200
        pass

    def lineplot(self, data: DataFrame, x: str, y: str) -> Image:
        """
        Método lineplot: Gera um gráfico de linha do tipo imagem PIL.

        Parâmetros:

        data: Dataframe.

        x: str.

        y: str.


        Descrição dos parâmetros:

        data -> Argumento onde o usuário fornece um conjunto de dados em formato de dataframe.

        x -> Argumento onde o usuário fornece a coluna do dataframe fornecido que ele deseja utilizar como eixo x.

        y -> Argumento onde o usuário fornece a coluna do datafame fornecido que ele deseja utilizar como eixo y.

        
        Exemplo de uso:

        analise = Anaylzes()

        df = 'caminho_do_seu_dataframe'

        grafico_linha = analise.lineplot(data=df, x='Coluna_1', y='Coluna_2')
        
        grafico_linha.show()
        """
        logger.info('Gerando gráfico de linha...')
        fig, ax = plt.subplots()
        sns.lineplot(x=x, y=y, data=data, ax=ax)
        img = BytesIO()
        fig.savefig(img, format='png')
        img.seek(0)
        plt.close(fig)
        grafico = Image.open(io.BytesIO(img.read()))
        return grafico

    def barplot(self, data: DataFrame, x: str, y: str) -> Image:
        """
        Método barplot: Gera um gráfico de barras do tipo imagem PIL.

        Parâmetros:

        data: Dataframe.

        x: str.

        y: str.


        Descrição dos parâmetros:

        data -> Argumento onde o usuário fornece um conjunto de dados em formato de dataframe.

        x -> Argumento onde o usuário fornece a coluna do dataframe fornecido que ele deseja utilizar como eixo x.

        y -> Argumento onde o usuário fornece a coluna do datafame fornecido que ele deseja utilizar como eixo y.

        
        Exemplo de uso:

        analise = Anaylzes()

        df = 'caminho_do_seu_dataframe'

        grafico_barras = analise.barplot(data=df, x='Coluna_1', y='Coluna_2')
        
        grafico_barras.show()
        """
        logger.info('Gerando gráfico de barra...')
        rcParams['figure.figsize'] = (16, 10)
        fig, ax = plt.subplots()
        sns.barplot(data=data, x=x, y=y, estimator="sum")
        ax.set_title(f"Consumidores {y} por {x}")
        for p in ax.patches:
            height = p.get_height()
            ax.text(p.get_x()+p.get_width()/2., height+3, '{:1.2f}'.format((height+3)), ha='center')
        img = BytesIO()
        fig.savefig(img, format='png', dpi=self.__dpi)
        img.seek(0)
        plt.close(fig)
        grafico = Image.open(io.BytesIO(img.read()))
        return grafico

    def dispersao_plot(self, data1: DataFrame, data2: DataFrame, x_label: str, y_label: str, coluna_referencia: str, titulo: str) -> Image:
        """
        Método dispersao_plot: Gera um gráfico de dispersão do tipo imagem PIL.

        Parâmetros:

        data1: Dataframe.

        data2: Dataframe.

        coluna_referencia: str.

        x_label: str.

        y_label: str.

        titulo: str


        Descrição dos parâmetros:

        data1 -> Argumento onde o usuário fornece um conjunto de dados em formato de dataframe.

        data2 -> Argumento onde o usuário fornece o segundo conjunto de dados em formato de dataframe.

        x_label -> Argumento onde o usuário fornece a legenda que deseja exibir no eixo x. 

        y_label -> Argumento onde o usuário fornece a legenda que deseja exibir no eixo y.

        coluna_referencia -> Argumento onde o usuário fornece o nome da coluna em comum que se encontra nos dois dataframes e que será comparada.

        titulo -> Argumento onde o usuário fornece o título que dejesa para o seu gráfico.

        
        Exemplo de uso:

        analise = Anaylzes()

        df1 = 'caminho_do_seu_dataframe1'
        
        df2 = 'caminho_do_seu_dataframe2'

        grafico_dispersao = analise.dispersao_plot(data1=df1, data2=df2, x_label='Legenda do eixo x', y_label= 'Legenda do eixo y', coluna_referencia='Coluna', titulo: 'Esse é o título do meu gráfico')
        
        grafico_dispersao.show()

        NOTA:

        certifique-se que a coluna de referência nos dois dataframes estejam com o mesmo nome.

        Exemplo: 
        
        O usuário possui dois dataframes, um dataframe de vendas de um produto, e um dataframe de lucro obtido com esse produto.

        Caso queira comparar a dispersão entre os dois dataframes, utilize uma coluna em comum entre as duas, ex: Produto4
        """        
        if coluna_referencia in ['Poder Publico', 'Iluminacao Publica', 'Servico Publico', 'Consumo Proprio']:
            logger.info('Gerando gráfico de dispersão...')
            coluna2 = coluna_referencia.replace(' ','_') 
            rcParams['figure.figsize'] = (16,10)
            fig, ax = plt.subplots()
            plt.scatter(data1[coluna_referencia], data2[coluna2]/1000)
            plt.title(titulo)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            formatter = ticker.ScalarFormatter(useMathText=True)
            formatter.set_scientific(False)
            formatter.set_powerlimits((-1,1))
            plt.gca().yaxis.set_major_formatter(formatter)
            plt.gca().xaxis.set_major_formatter(formatter)
            img = BytesIO()
            fig.savefig(img, format='png', dpi=self.__dpi)
            img.seek(0)
            plt.close(fig)
            grafico = Image.open(io.BytesIO(img.read()))
            return grafico
        else:
            logger.info('Gerando gráfico de dispersão...')
            rcParams['figure.figsize'] = (16,10)
            fig, ax = plt.subplots()
            plt.scatter(data1[coluna_referencia], data2[coluna_referencia]/1000)
            plt.title(titulo)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            formatter = ticker.ScalarFormatter(useMathText=True)
            formatter.set_scientific(False)
            formatter.set_powerlimits((-1,1))
            plt.gca().yaxis.set_major_formatter(formatter)
            plt.gca().xaxis.set_major_formatter(formatter)
            img = BytesIO()
            fig.savefig(img, format='png', dpi=self.__dpi)
            img.seek(0)
            plt.close(fig)
            grafico = Image.open(io.BytesIO(img.read()))
            return grafico

    def pointplot(self, data: DataFrame, x: str, y: str, title: str, x_label: str, y_label: str, hue:str=None) -> Image:
        """
        Método pointplot: Gera um gráfico de linha com pontos do tipo imagem PIL.

        Parâmetros:

        data: Dataframe.

        x: str.

        y: str.

        title: str.

        x_label: str.

        y_label: str.

        hue: str.


        Descrição dos parâmetros:

        data -> Argumento onde o usuário fornece um conjunto de dados em formato de dataframe.

        x -> Argumento onde o usuário fornece a coluna do dataframe fornecido que ele deseja utilizar como eixo x.

        y -> Argumento onde o usuário fornece a coluna do datafame fornecido que ele deseja utilizar como eixo y.

        title -> Argumento onde o usuário fornece o título do gráfico.

        x_label -> Argumento onde o usuário fornece a legenda do eixo x.

        y_label -> Argumento onde o usuário fornece a legenda do eixo y.

        hue -> Argumento onde o usuário fornece a coluna do dataframe responsável por segregar os dados.

        
        Exemplo de uso:

        analise = Anaylzes()

        df = 'caminho_do_seu_dataframe'

        grafico_pontos = analise.pointplot(data=df, x='Coluna_1', y='Coluna_2', title='Titulo do gráfico', x_label='Legenda do eixo x', y_label='Legenda do eixo y', hue='Coluna_5')
        
        grafico_pontos.show()

        NOTA: 

        Nesse exemplo de uso, repare que o hue é a coluna 5 do dataframe, imagine que esse dataframe em questão na coluna 5 tenha informações de classificação.

        E esse dataframe está com as seguintes classificações: Pequeno, Médio e Grande.

        Quando o gráfico for plotado, irá ter 3 linhas, uma para cada classificação.

        O argumento hue NÃO É OBRIGATÓRIO
        """
        logger.info('Gerando gráfico de pontos...')
        rcParams['figure.figsize'] = (16, 10)
        fig, ax = plt.subplots()
        sns.pointplot(data=data, x=x, y=y, hue=hue)
        ax.set_title(title)
        ax.legend()
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.grid(True)
        img = BytesIO()
        fig.savefig(img, format='png', dpi=self.__dpi)
        img.seek(0)
        plt.close(fig)
        grafico = Image.open(io.BytesIO(img.read()))
        return grafico
    
    def boxplot(self, data: DataFrame, column: str, x_label: str) -> Image:
        """
        Método boxplot: Gera um gráfico de caixa do tipo imagem PIL.

        Parâmetros:

        data: Dataframe.

        column: str.

        x_label: str.


        Descrição dos parâmetros:

        data -> Argumento onde o usuário fornece um conjunto de dados em formato de dataframe.

        column -> Argumento onde o usuário fornece a coluna que ele deseja fazer a análise de outliers.

        Exemplo de uso:

        analise = Anaylzes()

        df = 'caminho_do_seu_dataframe'

        grafico_caixa = analise.boxplot(data=df, column='Coluna_3', x_label='Outliers da coluna 3')
        
        grafico_caixa.show()
        """

        logger.info('Gerando gráfico de caixa (boxplot)...')
        rcParams['figure.figsize'] = (16, 10)
        fig, ax = plt.subplots()
        sns.boxplot(data=data[column]).set(xlabel=x_label)
        img = BytesIO()
        fig.savefig(img, format='png', dpi=self.__dpi)
        img.seek(0)
        plt.close(fig)
        grafico = Image.open(io.BytesIO(img.read()))
        return grafico

    def grafico_de_barras_e_linha(self, dataBarra: DataFrame, dataLinha: DataFrame, coluna_em_comum: str, coluna_barra: str, coluna_linha, x_label: str, y_label_barra: str, y_label_linha: str, title: str) -> Image:
        """
        Método grafico_de_barras_e_linhas: Gera um gráfico de barras com linha do tipo imagem PIL.

        Parâmetros:

        dataBarra: Dataframe.

        dataLinha: Dataframe.

        coluna_em_comum: str.

        coluna_barra: str.

        coluna_linha: str.

        x_label: str.

        y_label_barra: str.

        y_label_linha: str.

        title: str.


        Descrição dos parâmetros:

        dataBarra -> Argumento onde o usuário fornece o conjunto de dados desejado para ser representado em barra, no formato Dataframe.

        dataLinha -> Argumento onde o usuário fornece o conjunto de dados desejado para ser representado em linha, no formato Dataframe.

        coluna_em_comum -> Argumento onde o usuário fornece a coluna do dataframe em que vai ser comparada pelos dois.

        coluna_barra -> Argumento onde o usuário fornece a coluna do dataframe em que vai ser usada para a barra.

        coluna_linha -> Argumento onde o usuário fornece a coluna do dataframe em que vai ser usada para a linha.

        x_label -> Argumento onde o usuário coloca a legenda do eixo x.

        y_label_barra -> Argumento onde o usuário coloca a legenda do eixo y da barra.

        y_label_linha -> Argumento onde o usuário coloca a legenda do eixo y da linha.

        title -> Argumento onde o ususário coloca o título dog gráfico.

        
        Exemplo de uso:

        analise = Anaylzes()

        df1 = 'caminho_do_seu_dataframe'

        df2 = 'caminho_do_seu_segundo_dataframe'

        grafico_barras_e_linha = analise.grafico_de_barras_e_linha(dataBarra=df1, dataLinha= df2, coluna_em_comum='Pets', coluna_barra='Pets_Vendas', coluna_linha='Pets_inflação', x_label='Pets', y_label_barra= 'Vendas de itens de pets', y_label_linha='Inflação sobre os produtos', title='Relação vendas de itens de pets com inflação sobre os produtos')
        
        grafico_barras_e_linha.show()

        """

        logger.info('Gerando gráfico de barra com linha...')
        rcParams['figure.figsize'] = (16, 10)
        # criar o plot com barras para o PIB
        fig, ax1 = plt.subplots(figsize=(8, 6))
        ax1.bar(dataBarra[coluna_em_comum], dataBarra[coluna_barra], alpha=0.5, color='b')

        # criar o segundo eixo y para o consumo
        ax2 = ax1.twinx()
        ax2.plot(dataLinha[coluna_em_comum], dataLinha[coluna_linha], color='r', linewidth=3, marker='o')

        # definir os rótulos dos eixos e o título do gráfico
        ax1.set_xlabel(x_label)
        ax1.set_ylabel(y_label_barra, color='b')
        ax2.set_ylabel(y_label_linha, color='r')
        plt.title(title)
        img = BytesIO()
        fig.savefig(img, format='png', dpi=self.__dpi)
        img.seek(0)
        plt.close(fig)
        grafico = Image.open(io.BytesIO(img.read()))
        return grafico
    
    def matriz_corr(self, data: DataFrame, colunas: list = []) -> Image:
        """
        Método matriz_corr: Gera um gráfico de matriz de correlação do tipo imagem PIL.

        Parâmetros:

        data: Dataframe.

        colunas: list.


        Descrição dos parâmetros:

        data -> Argumento onde o usuário fornece um conjunto de dados em formato de dataframe.

        colunas -> Argumento onde o usuário fornece uma lista com as colunas que deseja utilizar para a correlação.

        Exemplo de uso:

        analise = Anaylzes()

        df = 'caminho_do_seu_dataframe'

        grafico_matriz_corr = analise.matriz_corr(data=df, colunas=['Coluna_1', 'Coluna_7', 'Coluna_4'])
        
        grafico_matriz_corr.show()

        NOTA:

        O argumento de colunas NÃO É OBRIGATÓRIO
        """
        # Correlation
        logger.info('Gerando gráfico de matriz de correlação...')
        rcParams['figure.figsize'] = (30, 20)
        fig, ax = plt.subplots()
        if colunas:
            corr_mat = data[colunas].corr()
        else:
            corr_mat = data.corr()
        mask = np.array(corr_mat)
        mask[np.tril_indices_from(mask)] = False
        sns.heatmap(corr_mat, mask=mask, square=True, annot=True)
        img = BytesIO()
        fig.savefig(img, format='png', dpi=self.__dpi)
        img.seek(0)
        plt.close(fig)
        grafico = Image.open(io.BytesIO(img.read()))
        return grafico
    
    def correlacao(self, data: DataFrame, colunas: list = []) -> list:
        """
        Método correlacao: Gera uma tabela de correlação entre as colunas.

        Parâmetros:

        data: Dataframe.

        colunas: list.


        Descrição dos parâmetros:

        data -> Argumento onde o usuário fornece um conjunto de dados em formato de dataframe.

        colunas -> Argumento onde o usuário fornece uma lista com as colunas que deseja utilizar para a correlação.

        Exemplo de uso:

        analise = Anaylzes()

        df = 'caminho_do_seu_dataframe'

        graifico_correlacao = analise.correlacao(data=df, colunas=['Coluna_3', 'Coluna_20', 'Coluna_13'])
        
        print(grafico_correlacao)

        NOTA:

        O argumento de colunas NÃO É OBRIGATÓRIO
        """
        logger.info('Gerando informações de correlação...')
        correlacao = data[colunas].corr()

        return correlacao
    

class DataProcess:
    name_sheets = []
    sheet_selected = pd.DataFrame
    def __init__(self, data: str) -> None:
        self.data = pd.ExcelFile(data)
        self.__name_sheets = self.data.sheet_names
    """
    Class DataProcess
    Classe responsável por pegar uma planilha do excel e processar ela.
    :param data: str.
    """
    def sheets(self) -> list:
        """
        Retorna uma lista com os nomes de todas as abas da planilha.
        """
        logger.info('Gerando lista com nomes das abas do excel...')
        return self.__name_sheets
    
    def sheet_select(self, sheet: str) -> DataFrame:
        """
        Retorna a aba selecionada da planilha em formato de DataFrame.
        :param sheet: str
        """
        logger.info('Selecionando aba do excel escolhida...')
        self.sheet_selected = pd.read_excel(self.data, sheet_name=sheet)

        return self.sheet_selected
    

class Treatment:
    def __init__(self) -> None:
       self.colunas_vazias = []
       pass

    def add_column_year(self, data: DataFrame, column: str) -> DataFrame:
        logger.info('Adcionando coluna de ano...')
        self.data = data.copy()
        self.data.loc[:, 'Ano'] = self.data[column].apply(lambda x: x.year)
        logger.info('Coluna de ano adiciona com suceso!')
        return self.data
    
    def add_column_month(self, data: DataFrame, column: str) -> DataFrame:
        logger.info('adicionando coluna de mês...')
        self.data = data.copy()
        self.data.loc[:, 'Mês'] = self.data[column].apply(lambda x: x.month)
        logger.info('Coluna de mês adicionada com sucesso!')
        return self.data
    
    def add_column_day(self, data: DataFrame, column: str) -> DataFrame:
        logger.info('adicionando coluna de dia...')
        self.data = data.copy()
        self.data.loc[:, 'Dia'] = self.data[column].apply(lambda x: x.day_name())
        logger.info('Coluna de dia adicionada com sucesso!')
        return self.data

    def treatment_of_missing_data(self, data: DataFrame, treatment: str) -> DataFrame:
        match treatment:
            case "remove":
                logger.info('removendo valores nulos...')
                self.data = data.copy()
                self.data = data.dropna()
                logger.info('Valores nulos removidos com sucesso!')
                return self.data
            case "average":
                logger.info("preenchendo os valores nulos com a média dos dados...")
                self.data = data.copy()
                self.data = data.fillna(data.mean(), inplace=True)
                logger.info('Valores nulos preenchidos pela média com sucesso!')
                return self.data
            case "zero":
                logger.info("prenchendo os valores nulos com zero...")
                self.data = data.copy()
                self.data = data.fillna(0, inplace=True)
                logger.info('Valores nulos preenchidos por zero com sucesso!')
                return self.data
            case _:
                 raise KeyError('Por favor, insira remover para remover valores nulos, media para preencher com a média os valores nulos ou zero para preencher com zero os valores nulos!')
    
    def date_range(self, data: DataFrame, start_date: str, end_date: str, data_column: str) -> DataFrame:
        logger.info('filtrando por intervalo de datas')
        self.data = data.copy()
        self.data = data.loc[(data[data_column] >= start_date) & (data[data_column] <= end_date)]
        logger.info(f'Dataframe filtrado no intervalo de {start_date} até {end_date} com sucesso!')
        return self.data
    
    def year_range(self, data: DataFrame, start_year: int, end_year: int, year_column: str) -> DataFrame:
        logger.info('filtrando por intervalo de ano...')
        self.data = data.copy()
        self.data = data.loc[(data[year_column] >= start_year) & (data[year_column] <= end_year)]
        logger.info(f'Dataframe filtrado no intervalo de {start_year} até {end_year} com sucesso!')
        return self.data
    
    def column_range(self, data: DataFrame, start_column: str, end_column: str) -> DataFrame:
        logger.info('filtrando por intervalo de colunas...')
        self.data = data.copy()
        self.data = data.loc[:, start_column:end_column]
        logger.info(f'Dataframe filtrado no intervalo de colunas da coluna {start_column} até a coluna {end_column} com sucesso!')
        return self.data
    
    def convert_json_to_dataframe(self, json_file: json) -> DataFrame:
        logger.info('Transformando json em dataframe...')
        # Lendo o arquivo JSON em um dicionário
        with open(json_file, 'r') as f:
            data = json.load(f)

        # Convertendo o dicionário em um DataFrame
        df = pd.DataFrame.from_dict(data)
        logger.info('Json transformado para Dataframe com sucesso!')
        return df
    
    def check_column_with_null_values(self, data: DataFrame) -> list[str]:
        logger.info('Checando colunas com valores nulos...')
        columns_with_null_values = data.columns[data.isnull().any()].tolist()
        logger.info('Colunas com valores nulos checadas com sucesso!')
        return columns_with_null_values
    
    def remove_column(self, data: DataFrame, column: str = None, index: int = None, last: str = None) -> DataFrame:

        if index == None and column != None:
            logger.info('Removendo coluna...')
            data = data.drop(column, axis=1)
            logger.info('Coluna removida com sucesso!')
            return data
        elif column == None and index != None:
            logger.info('Removendo coluna...')
            data = data.pop(data.columns[index])
            logger.info('Coluna removida com sucesso!')
            return data
        elif last == 'yes':
            logger.info('Removendo a última coluna...')
            data = data.iloc[:,:-1]
            logger.info('Última coluna removida com sucesso!')
            return data
        else:
            raise Exception('Error')

    def remove_row(self, data: DataFrame, index: int) -> DataFrame:
        logger.info('Removendo linha...')
        data = data.drop(index, axis=0)
        data = data.reset_index(drop=True)
        logger.info('Linha removida com sucesso!')
        return data
    
    def convert_dataframe_to_json(self, data: DataFrame, json_path: str) -> json:
        logger.info('Transformando dataframe em json...')
        dados_dict = data.to_dict(orient='records')
        dados_json = json.dumps(dados_dict)

        try:
            with open(json_path, 'w') as json_file:
                json_file.write(dados_json)
            
            logger.info('Dataframe transformado para json com sucesso!')
            return 0
        except Exception as e:
            print(f'Erro no processo da transformação! {str(e)}')
            return 1
    
    def dataframe_for_a_row(self, data: DataFrame, index: int) -> DataFrame:
        logger.info('Gerando um dataframe a partir de uma linha...')
        df = data.iloc[index:]
        df = df.reset_index(drop=True)
        logger.info('Dataframe gerado com sucesso!')
        return df
    
    def turn_row_into_header(self, data: DataFrame, index: int) ->  DataFrame:
        logger.info('Transformando linha em cabeçalho...')
        df = data.set_axis(data.iloc[index], axis=1)
        df = df[index+1:]
        logger.info('Linha transformada em cabeçalho com sucesso!')
        return df
    
    def change_data_type(self, data: DataFrame, column: str, type: str) -> DataFrame:
        logger.info('Alterando tipo de dados...')

        match type:
            case 'datetime':
                data[column] = pd.to_datetime(data[column])
                logger.info(f'Coluna {column} alterada para datetime com sucesso!')
                return data
            case _:
                return 'error'
    
    def replace_value_in_a_position(self, data: DataFrame, column: int, row: int, name: str) -> DataFrame:
        logger.info('Substituindo um valor em uma posição...')
        data.iloc[column, row] = name
        logger.info('Valor substituido com sucesso!')
        return data