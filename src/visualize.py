matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm
matplotlib.rcParams['font.family'] = 'UnDotum'
matplotlib.rcParams['axes.unicode_minus'] = False
if 'lang' in args.input_path:
    file_type = "Language"
else:
    file_type = "Country"

plt.bar(top_10, top_10_values, width=1, edgecolor="white", linewidth=0.7)
plt.title("Tweets with " + args.key + " by " + file_type)
plt.ylabel("Number of tweets")
plt.xlabel(file_type)
plt.tight_layout()
plt.savefig(args.output_png)

plt.show()
