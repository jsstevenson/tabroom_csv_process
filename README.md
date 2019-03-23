# README

## Usage

Tabroom CSV --> ballots CSV

```bash
$ python3 tabroom_csv_process [path-to-folder-to-process]
```

## Omissions/Working

### 2017-2018
* Kentucky: no speaker points for JV or novice. Not included until that's dug up.
* UCF: no round-by-round results (nor cumulatives?). Not included.
* CSUF Fall: no results posted.
* NW Fall Champs: novice speaks not posted
* Cal Swing 1: Open finals missing 1 vote
* Miami: Novice breakout finals results look wonky (judge decisions appear differently on each team's results page). Not included.
* Pitt RR: Results posted to CEDA forums don't list sides -- waiting to include until that can be dug up. Would also appreciate a more digestable format.
* New School: Open finals don't list complete ballot results
* D6: Results don't list speaks; holding off on adding them until that's filled in.
* D4: basically no results
* D8: No speaks!
* ADA: No speaks in open and jv (but yes for novice?)

### 2016-2017
* Rochester: no speaker points, not included for now.
* UNI: no speaker points, not included for now.
* Rutgers: no speaker points
* Golden Gate Opener: no speaker points
* West Point: no speaker points
* KCKCC: no JV/novice results (I think this is on purpose - but noting for now)
* Gonzaga: finals?
* Vermont: no speaks
* UCO: no speaks
* Monmouth: no speaks
* ADA Fall: Something wonky happened with sems results but I assumed that the half-complete speaker points were deletable
* Wake: finals?
* Illinois college: no results
* West Georgia: no results
* Southwestern: novice round 4 breaks me for some reason.
* Indiana: novice prelim results aren't showing up under "results"
* Gotham Scrikmmage: no speaks
* Cornell: no speaks
* MAC: no results (novice) or speaks (open)
* D6: no speaks
* D5: no speaks. But they might not have been assigned. I need to think about how to categorize this (an "elim-style" prelim?)
* Binghamton NE Regional: no speaks
* D8: no speaks
* D7: no speaks
* D4: no results
* JV/novice nats WVU: no speaks
* NJDDT: no novice speaks

### 2015-2016
* UNI: no novice results
* Weber: no JV finals
* UCF: no results


### 2013-2014
* NDT: There's some weirdness going on with some Indiana entries (I think drops?). I pulled those rounds out for now.



## Ideas for running data

* Most pref'd judges: gather round commitment data (eugh) and divide by rounds judged
* 1st round voting stuff
* ELO stuff
  * Likelihood of upsets dependent on various factors? Sides? location? Length of tournament
  * PageRank/Eigenvalue stuff vs ELO (recency bias good/bad?)
* Tournament distance/travel stuff
