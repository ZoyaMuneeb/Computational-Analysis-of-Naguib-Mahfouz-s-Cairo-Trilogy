import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display

# Load your data
df = pd.read_excel('Book3.xlsx', index_col=0)

# Fix Arabic text display
df.index = [get_display(arabic_reshaper.reshape(name)) for name in df.index]
df.columns = [get_display(arabic_reshaper.reshape(col)) if any('\u0600' <= c <= '\u06FF' for c in col) else col for col in df.columns]

# Create heatmap
plt.figure(figsize=(14, 8))
sns.heatmap(df, annot=True, fmt='d', cmap='YlOrRd', 
            linewidths=0.5, cbar_kws={'label': 'Collocate Count'})
plt.title('Character-Theme Collocate Analysis: Sugar Street', 
          fontsize=16, pad=20)
plt.xlabel('Themes', fontsize=12)
plt.ylabel('Characters', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('palace_of_desires_heatmap.png', dpi=300, bbox_inches='tight')
plt.show()