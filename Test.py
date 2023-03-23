import dplython as dpl
from dplython import (DplyFrame,
                      X,
                      diamonds,
                      dfilter,
                      select,
                      sift,
                      sample_n,
                      sample_frac,
                      head,
                      arrange,
                      mutate,
                      nrow,
                      group_by,
                      summarize,
                      DelayFunction)
head(diamonds,3)
priceCutWise = diamonds.groupby("cut")["price"].mean()
priceCutWise
