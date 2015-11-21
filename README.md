# code-jammer
Classifying lukemia.

<a href="https://gitter.im/itscharlieb/code-jammer" target="_blank">
  <img alt="Join Chat" src="https://badges.gitter.im/Join%20Chat.svg">
</a>

### Dataset

We are given a dataset of 166 patients to train our models. Each of the 166 patients has 269 features; an id, 265 predictive features, and 3 dependent target features. The structure of this dataset is described below.

|Column| 0 | 1 - 265| 266 | 267 | 268 |
|------|---|--------|-----|-----|-----|
|Value| id | Predictive Features | resp.simple | Remission_Duration | Overall_Survival |
|Data Types| string | misc. | COMPLETE_REMISSION, RESISTANT | N/A, float | float |
|Description| identification | Described in more detail below | Remission type | Length of remssion in days | Days lived since diagnosis |
