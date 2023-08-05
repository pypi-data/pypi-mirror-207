# 首先引入包
import numpy as np
import matplotlib.pyplot as plt
import math as mt

class GM:
    def __init__(self,x,t,dt,num_prediction=1):
        # 原始序列
        self.X0 = x
        # X0[0] 开始值
        self.t = t
        self.dt = dt
        # 预测点数
        self.num_prediction = num_prediction
        self.x_hat=None

    def calc(self):
        # 计算轴向元素累加和
        X1 = [self.X0[0]]
        add = self.X0[0] + self.X0[1]
        X1.append(add)
        i = 2
        while i < len(self.X0):
            add = add + self.X0[i]
            X1.append(add)
            i += 1
        print("X1", X1)
        M = []
        j = 1
        while j < len(X1):
            num = (X1[j] + X1[j - 1]) / 2
            M.append(num)
            j = j + 1
        print("M", M)

        # 最小二乘法
        Y = []
        x_i = 0
        while x_i < len(self.X0) - 1:
            x_i += 1
            Y.append(self.X0[x_i])
        Y = np.mat(Y).T
        Y.reshape(-1, 1)
        print("Y", Y)
        B = []
        b = 0
        while b < len(M):
            B.append(-M[b])
            b += 1
        print("B:", B)
        B = np.mat(B)
        B.reshape(-1, 1)
        B = B.T
        c = np.ones((len(B), 1))
        B = np.hstack((B, c))
        print("c", c)
        print("b", B)

        # 设置参数
        beta = np.linalg.inv(B.T.dot(B)).dot(B.T).dot(Y)
        a = beta[0]
        u = beta[1]
        print("a = ",a)
        print("u = ",u)
        const = u / a
        print(beta)
        print(type(beta))

        # 预测模型
        F = [self.X0[0]]
        k = 1
        while k < len(self.X0) + self.num_prediction:
            F.append((self.X0[0] - const) * mt.exp(-a * k) + const)
            k += 1
        print("F", F)
        # 输出预测模型
        print(f"X(1,K+1) = {[self.X0[0]-u/a][0]}e^({-a}k)+{u/a}")

        # 得到预测序列
        x_hat = [self.X0[0]]
        g = 1
        while g < len(self.X0) + self.num_prediction:
            print(g)
            x_hat.append(F[g] - F[g - 1])
            g += 1
        self.X0 = np.array(self.X0)
        self.x_hat = np.array(x_hat)
        print(x_hat)

    def show_figure(self):
        # 设置时间序列
        t1 = range(self.t, self.t+len(self.X0),self.dt)
        t2 = range(self.t, self.t+len(self.X0) + self.num_prediction*self.dt,self.dt)

        # 结果可视化
        plt.plot(t1, self.X0, color='r', linestyle="--", label='true')
        plt.plot(t2, self.x_hat, color='b', linestyle="--", label="predict")
        plt.legend(loc='upper right')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Prediction by Grey model')
        plt.show()

    def run(self,show_figure=False):
        self.calc()
        if show_figure:
            self.show_figure()