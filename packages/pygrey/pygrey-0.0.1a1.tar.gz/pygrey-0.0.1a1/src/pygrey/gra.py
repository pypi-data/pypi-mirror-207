import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class GRA:
    def __init__(self,data_path,use_cols):
        # 从硬盘读取数据进入内存
        self.data = pd.read_excel(data_path, usecols=use_cols)
        print()
        print(self.data)

    # 无量纲化
    def dimensionlessProcessing(self,df):
        newDataFrame = pd.DataFrame(index=df.index)
        columns = df.columns.tolist()
        for c in columns:
            d = df[c]
            MAX = d.max()
            MIN = d.min()
            MEAN = d.mean()
            # newDataFrame[c] = ((d - MEAN) / (MAX - MIN)).tolist()
            newDataFrame[c] = (d/ d[0]).tolist()
            # newDataFrame[c] = (d/ MEAN).tolist()
        return newDataFrame

    def GRA_ONE(self,gray, m=0):
        # 读取为df格式
        gray = self.dimensionlessProcessing(gray)
        print()
        print(gray)
        # 标准化
        std = gray.iloc[:, m]  # 为标准要素
        gray.drop(str(m),axis=1,inplace=True)
        ce = gray.iloc[:, 0:]  # 为比较要素
        shape_n, shape_m = ce.shape[0], ce.shape[1]  # 计算行列
        # 与标准要素比较，相减
        a = np.zeros([shape_m, shape_n])
        for i in range(shape_m):
            for j in range(shape_n):
                a[i, j] = abs(ce.iloc[j, i] - std[j])
        # 取出矩阵中最大值与最小值
        c, d = np.amax(a), np.amin(a)
        # 计算值
        result = np.zeros([shape_m, shape_n])
        for i in range(shape_m):
            for j in range(shape_n):
                result[i, j] = (d + 0.5 * c) / (a[i, j] + 0.5 * c)

        # 求均值，得到灰色关联值,并返回
        result_list = [np.mean(result[i, :]) for i in range(shape_m)]
        result_list.insert(m,1)
        return pd.DataFrame(result_list)

    def GRA(self,DataFrame):
        df = DataFrame.copy()
        list_columns = [
            str(s) for s in range(len(df.columns)) if s not in [None]
        ]
        df_local = pd.DataFrame(columns=list_columns)
        df.columns=list_columns
        for i in range(len(df.columns)):
            df_local.iloc[:, i] = self.GRA_ONE(df, m=i)[0]
        return df_local

    # 灰色关联结果矩阵可视化
    def ShowGRAHeatMap(self,DataFrame):
        colormap = plt.cm.RdBu
        ylabels = DataFrame.columns.values.tolist()
        f, ax = plt.subplots(figsize=(14, 14))
        ax.set_title('GRA HeatMap')
        # 设置展示一半，如果不需要注释掉mask即可
        mask = np.zeros_like(DataFrame)
        mask[np.triu_indices_from(mask)] = True
        DataFrame=np.float32(DataFrame)
        with sns.axes_style("white"):
            sns.heatmap(DataFrame,
                        cmap="YlGnBu",
                        annot=True,
                        mask=mask,
                        )
        plt.show()

    def run(self,show_fig=False):
        # 处理数据
        data_wine_gra = self.GRA(self.data)
        if show_fig:
            # 展示分析结果
            self.ShowGRAHeatMap(data_wine_gra)


