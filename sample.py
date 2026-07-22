import re
from pathlib import Path
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams["font.family"] = "Hiragino Sans"

base_dir = Path(__file__).parent

csv_path = base_dir / "data" / "kion.csv"


tourist = '768.712| 540.394| 423.698| 461,105| 648.124| 737.155| 504.239| 1.920.136| 613.025| 735.671| 452.022| 376,498\n'

temperatures = pd.read_csv(csv_path,encoding="utf-8")

print(temperatures)

temperature_df = pd.read_csv(
    csv_path,
    encoding="utf-8"
)

print("行・列数:", temperature_df.shape)
print("列名:", temperature_df.columns.tolist())
print(temperature_df.head())

temperature_df =temperature_df.dropna(how="all").copy()

temperature_values = temperature_df["平均気温(℃)"].tolist()

print(temperature_values)
print("気温データ数:", len(temperature_values))

tourist_texts = re.findall(r"\d[\d.,]*",tourist)

tourist_values = [
    int(re.sub(r"[,.]", "", value))
    for value in tourist_texts
]

print(tourist_values)
print("観光客データ数:", len(tourist_values))

analysis_df = pd.DataFrame({
    "年月": temperature_df["年月"].tolist(),
    "平均気温": temperature_values,
    "観光客数": tourist_values
})

print(analysis_df)

sns.regplot(
    data=analysis_df,
    x="平均気温",
    y="観光客数",
    ci=95,
    color="red",
    scatter_kws={
        "color": "orange",
        "s": 60,
        "alpha": 0.8
    },
    line_kws={
        "color": "red"
    }
)

for _, row in analysis_df.iterrows():
    plt.annotate(
        str(row["年月"]),
        (row["平均気温"], row["観光客数"]),
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=8
    )
    
    correlation = analysis_df["平均気温"].corr(
    analysis_df["観光客数"]
)

# グラフを作る既存コード

image_dir = base_dir / "images"
image_dir.mkdir(exist_ok=True)

plt.savefig(
    image_dir / "temperature_tourism_analysis.png",
    dpi=200,
    bbox_inches="tight"
)

plt.show()

print("相関係数:", correlation)

image_dir = base_dir / "images"
image_dir.mkdir(exist_ok=True)

plt.savefig(
    image_dir / "temperature_tourism_analysis.png",
    dpi=200,
    bbox_inches="tight"
)

saved_image = image_dir / "temperature_tourism_analysis.png"

print("画像保存先:", saved_image.resolve())
print("画像あり:", saved_image.exists())

plt.show()


