# bkai-polyp-assignment

Dataset is from [BKAI-IGH NeoPolyp](https://www.kaggle.com/competitions/bkai-igh-neopolyp/data)

You can find the checkpoint file [here](https://drive.google.com/file/d/1s_azXYekjo3nLu3iF5cBP5GHgZTVQOzL/view?usp=sharing). For inference, the file need to be placed inside model folder in this repository.

Code for cloning the repository to local workspace:

```
git clone https://github.com/quangtranngoc/bkai-polyp-assignment.git
```

Change current working directory to this repository:

```
cd bkai-polyp-assignment
```

Make inference from your image:

```
python3 infer.py "path/to/image" "path/to/destination"
```
or

```
python infer.py "path/to/image" "path/to/destination"
```
