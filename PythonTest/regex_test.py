# %%
import re

# %%

text = "This is a lot of text"
# x = re.search(r"[Tt]his", text)
x = re.findall(r"[Tt]", text)


print(x)
# %%
