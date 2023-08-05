## PyGrey
This toolkit provides implementation of Grey Relation Analysis and Grey Model Prediction. 

### Example

- Grey Relation Analysis (GRA)

```python
from pygrey.gra import *
# Grey Relation Analysis (GRA)
# load data from an Excel file
gra=GRA(data_path='data/data.xlsx',use_cols=[0,1,2,3])
# run the model
gra.run(show_fig=True)
```

- Grey Model Prediction (GM(1,1))
```python
from pygrey.gm import *
# Sequence
X0 = [7413.7, 7579, 7739.2, 7696, 7787.7, 7584.1, 7489, 7355, 7138]
# X axis
t = 1996
dt = 1
# Number of prediction
num_prediction = 2
# Grey model
gm=GM(x=X0,t=t,dt=dt,num_prediction=num_prediction)
# run the model
gm.run(show_figure=True)
```

Other GM implementation:

```python
from pygrey.gm_v2 import *
ls = [7413.7, 7579, 7739.2, 7696, 7787.7, 7584.1, 7489, 7355, 7138]
gm = GM()
gm.fit(ls)
print("Confidennce = ",gm.confidence())
print("X0 = ",ls)
print("Prediction = ", gm.predict(m=4))
```

### License

The `pygrey` project is provided by [Donghua Chen](https://github.com/dhchenx). 
