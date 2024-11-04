# Data-visualization
A data  visualization presentation for CS 131

Different Marker Styles:
marker_styles = [
    '.',  # Point
    ',',  # Pixel
    'o',  # Circle
    '^',  # Triangle up
    'v',  # Triangle down
    '<',  # Triangle left
    '>',  # Triangle right
    's',  # Square
    'D',  # Diamond
    '*',  # Star
    'p',  # Pentagon
    'h',  # Hexagon1
    'H',  # Hexagon2
    '+',  # Plus
    'x'   # Cross
]

Types of Plots:
Basic Plots
Line Plot: plot()
Scatter Plot: scatter()
Bar Chart: bar()
Horizontal Bar Chart: barh()
Pie Chart: pie()
Stem Plot: stem()
Step Plot: step()
Error Bar Plot: errorbar()
Fill Between Plot: fill_between()
Statistical Plots
Histogram: hist()
Box Plot: boxplot()
Violin Plot: violinplot()
Kernel Density Estimate (KDE) Plot: Requires seaborn for extended KDE functionality
Cumulative Distribution Function (CDF) Plot: ecdf() (using external libraries like seaborn)
Advanced Plot Types
Hexbin Plot: hexbin() (useful for large datasets)
2D Density Plot: Uses imshow() with density data, or contour() for contour mapping
Specialized Plot Types
Quiver Plot: quiver() (for vector fields)
Stream Plot: streamplot() (for continuous vector fields)
Polar Plot: polar()
Contour Plot: contour() for filled contour maps, contourf() for unfilled
Image Plot: imshow()
Heatmap: imshow() or pcolor() for gridded data visualization
3D Plots (Requires mpl_toolkits.mplot3d)
3D Line Plot: plot3D()
3D Scatter Plot: scatter3D()
3D Surface Plot: plot_surface()
3D Wireframe Plot: plot_wireframe()
3D Contour Plot: contour3D()
3D Bar Plot: bar3D()