import random
import statistics

WT_U = -0.75
WT_M = -0.5
WT_A = 0
WT_N = 1
WT_E = 1.5

# ---- Populate with convincing looking random data ----

slugs = {
    "A-01": r"$\theta \colon \mathbb Z[x] \to \mathbb Z$",
    "A-02": r"$\sqrt[3]{\frac{a}{b+7}}$",
    "A-03": r"$a^a b^b c^c$",
    "C-04": r"$a+2b+\dots+32c$",
    "C-05": r"$2017$-vtx dinner",
    "G-06": r"$ST$ orthog",
    "G-07": r"$PO \perp YZ$",
    "G-08": r"Area $5/2$",
    "G-09": r"$XD \cap AM$ on $\Gamma$",
    "G-10": r"$\angle PQE, \angle PQF = 90^{\circ}$",
    "N-11": r"$5^n$ has six zeros",
    "N-12": r"$n^2 \mid b^n+1$",
    "N-13": r"$fff$ cycles",
}

qualities = {}
difficulties = {}
random.seed(150)
for k in slugs.keys():
    # just somehow throw stuff at wall to get counts
    a, b, c, d, e, f = [random.randrange(0, 3) for _ in range(6)]
    if c >= 1:
        a = 0
    if a >= 2:
        d, e = 1, 0
    if e == 0:
        f = 0
    if a == 0 and b == 0:
        e *= 2
    qualities[k] = (
        [WT_U] * a
        + [WT_M] * b
        + [WT_A] * (b + d + e)
        + [WT_N] * (c + d + e)
        + [WT_E] * (c + e + f)
    )

random.seed(369)
for k in slugs.keys():
    # just somehow throw stuff at wall to get counts
    a, b, c, d, e = [random.randrange(0, 5) for _ in range(5)]
    if e >= 4:
        b = 0
        c //= 2
    elif e >= 3:
        a = 0
        b //= 2
    if a >= 3:
        e = 0
        d //= 3
    elif a >= 2:
        e = 0
        d //= 2
    difficulties[k] = [1] * a + [1.5] * b + [2] * c + [2.5] * d + [3] * e

# ---- End random data population ----


def avg(S):
    return statistics.mean(S) if len(S) > 0 else None


def median(S):
    return statistics.median(S) if len(S) > 0 else None


# criteria for inclusion on chart
criteria = lambda k: True


def get_color_string(x, scale_min, scale_max, color_min, color_max):
    if x is None:
        return r"\rowcolor{gray}"
    m = (scale_max + scale_min) / 2
    a = min(int(100 * 2 * abs(x - m) / (scale_max - scale_min)), 100)
    color = color_min if x < m else color_max
    return r"\rowcolor{%s!%d}" % (color, a) + "\n"


def get_label(key, slugged=False):
    if slugged:
        return r"{\scriptsize \textbf{%s} %s}" % (key, slugs.get(key, ""))
    else:
        return r"{\scriptsize \textbf{%s}}" % key


## Quality rating
def get_quality_row(key, data, slugged=True):
    a = avg(data)
    s = ("$%+4.2f$" % a) if a is not None else "---"
    color_tex = get_color_string(a, WT_U, WT_E, "Salmon", "green")
    row_tex = r"%s & %d & %d & %d & %d & %d & %s \\" % (
        get_label(key, slugged),
        data.count(WT_U),
        data.count(WT_M),
        data.count(WT_A),
        data.count(WT_N),
        data.count(WT_E),
        s,
    )
    return color_tex + row_tex


def print_quality_table(d, sort_key=None, slugged=True):
    items = sorted(d.items(), key=sort_key)
    print(r"\begin{tabular}{lcccccr}")
    print(r"\toprule Prob & U & M & A & N & E & Avg \\ \midrule")
    for key, data in items:
        print(get_quality_row(key, data, slugged))
    print(r"\bottomrule")
    print(r"\end{tabular}")


## Difficulty rating
def get_difficulty_row(key, data, slugged=False):
    a = avg(data)
    s = ("$%.3f$" % a) if a is not None else "---"
    color_tex = get_color_string(a, 1, 3, "cyan", "orange")
    row_tex = r"%s & %d & %d & %d & %d & %d & %s \\" % (
        get_label(key, slugged),
        data.count(1),
        data.count(1.5),
        data.count(2),
        data.count(2.5),
        data.count(3),
        s,
    )
    return color_tex + row_tex


def print_difficulty_table(d, sort_key=None, slugged=False):
    items = sorted(d.items(), key=sort_key)
    print(r"\begin{tabular}{l ccccc c}")
    print(r"\toprule Prob & 1 & 1.5 & 2 & 2.5 & 3 & Avg \\ \midrule")
    for key, data in items:
        print(get_difficulty_row(key, data, slugged))
    print(r"\bottomrule")
    print(r"\end{tabular}")


filtered_qualities = {k: v for k, v in qualities.items() if criteria(k)}
filtered_difficulties = {k: v for k, v in difficulties.items() if criteria(k)}


def print_everything(name, fn=None, flip_slug=False):
    if fn is not None:
        sort_key = lambda item: fn(item[0])
    else:
        sort_key = None
    print(r"\section{" + name + "}")
    if flip_slug:
        print_quality_table(filtered_qualities, sort_key, False)
        print_difficulty_table(filtered_difficulties, sort_key, True)
    else:
        print_quality_table(filtered_qualities, sort_key, True)
        print_difficulty_table(filtered_difficulties, sort_key, False)


# Start outputting content
print(r"""\documentclass[11pt]{scrartcl}
\usepackage{booktabs}
\usepackage[sexy]{evan}
\usepackage{tikz}
\usepackage{pgfplots}
\pgfplotsset{compat=1.17}

\begin{document}
\title{Example of ratings table with randomly generated data}
\maketitle

\setlength\tabcolsep{5pt}
""")


print(r"\section{All ratings}")
print_quality_table(qualities)
print_difficulty_table(difficulties)

print("\n" + r"\newpage" + "\n")
print_everything(
    "Beauty contest, by overall popularity", lambda p: (-avg(qualities[p]), p), False
)
print_everything(
    "Beauty contest, by subject and popularity",
    lambda p: (p[0], -avg(qualities[p]), p),
    False,
)
print("\n" + r"\newpage" + "\n")
print_everything(
    "Beauty contest, by overall difficulty", lambda p: (-avg(difficulties[p]), p), True
)
print_everything(
    "Beauty contest, by subject and difficulty",
    lambda p: (p[0], -avg(difficulties[p]), p),
    True,
)

print("\n")
print(r"\section{Scatter plot}")
print(r"\begin{center}")
print(r"\begin{tikzpicture}")
print(r"""\begin{axis}[width=0.9\textwidth, height=22cm, grid=both,
    xlabel={Average difficulty}, ylabel={Average suitability},
    every node near coord/.append style={font=\scriptsize},
    scatter/classes={A={red},C={blue},G={green},N={black}}]""")
print(r"""\addplot [scatter,
    only marks, point meta=explicit symbolic,
    nodes near coords*={\prob},
    visualization depends on={value \thisrow{prob} \as \prob}]""")
print(r"table [meta=subj] {")
print("X\tY\tprob\tsubj")
for p in qualities.keys():
    x = avg(difficulties[p])
    y = avg(qualities[p])
    if x is None or y is None:
        continue
    print("%0.2f\t%0.2f\t%s\t%s" % (x, y, p[2:], p[0]))
print(r"};")
print(r"\end{axis}")
print(r"\end{tikzpicture}")
print(r"\end{center}")

print(r"\end{document}")
