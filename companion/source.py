"""Read the most recent Garmin running session and measured split detail from FIT exports."""
from serve import page
INTERVAL=30
def snapshot(o,m):
    if o.get("mode") == "strava":
        from live import reading
        return reading(o,m)
    from fit_runs import runs,pace
    history,bad=runs(o,m)
    if not history:return dict(state="No running sessions",key="empty",pages=[page("GARMIN FIT","No runs","Add a running FIT file",f"{bad} unreadable files")])
    start,meters,seconds,laps,splits=history[-1]
    pages=[page("LAST RUN",f"{meters/1000:.2f} km",start.strftime("%Y-%m-%d UTC"),
           "Moving "+pace(seconds),"Pace "+pace(seconds*1000/meters)+"/km")]
    if splits:
        slow=max(range(len(splits)),key=splits.__getitem__)
        pages.append(page("SLOWEST KM",slow+1,"Elapsed "+pace(splits[slow])+"/km",f"{len(splits)} complete km"))
        for n in range(min(35,len(splits))):
            pages.append(page("KM "+str(n+1),pace(splits[n]),"Elapsed time / km","Interpolated distance trace"))
    else:
        for n,(d,t) in enumerate(laps[:36],1):
            pages.append(page("LAP "+str(n),pace(t*1000/d),f"{d/1000:.2f} km / {pace(t)}","Lap pace / km"))
    return dict(state="Garmin FIT / local",key=start.isoformat(),pages=pages)
