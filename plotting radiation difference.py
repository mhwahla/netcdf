fig = plt.figure(figsize=(12,8))                                 # create the figure and axes instances
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])                          
m = Basemap(llcrnrlon=-145.5,                                    # setup of basemap
                    llcrnrlat=1.,                               
                    urcrnrlon=-2.566,
                    urcrnrlat=46.352,
                    rsphere=(6378137.00,6356752.3142),
                    resolution='l',
                    area_thresh=1000.,
                    projection='lcc',
                    lat_1=50.,
                    lon_0=-100.,
                    ax=ax)
X, Y = m(*np.meshgrid(lons_subset, lats_subset))
Z = np.mean(rad_na_diff, axis=0)
colors = m.pcolor(X, Y, Z,cmap='jet')
cb = plt.colorbar(colors)                                        # add colorbar
cb.set_label(data[var].units)                                    # add units
m.drawlsmask()                                                   # draw a land-sea mask
m.drawcoastlines(linewidth=0.5)                                  # draw coastlines and political boundaries.
m.drawcountries()
m.drawstates()
parallels = np.arange(0.,80,20.)                                 # draw parallels and meridians.label on left and bottom of map.
m.drawparallels(parallels,labels=[1,0,0,1])
meridians = np.arange(10.,360.,30.)
m.drawmeridians(meridians,labels=[1,0,0,1])                      
ax.set_title(data[var].long_name)                                # add title                               
plt.show()
