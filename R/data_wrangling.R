##########################################
# Script for data cleaning and wrangling #
##########################################

library(here)
library(RColorBrewer)

data <- read.csv(here("data","forest_health_data.csv"))
# Thanks Ziya @ Kaggle for the dataset!

# Main question we want to answer with this dataset:
# which variables are related to tree health status?

# Sub-questions:
# Is _______ related to health tree status?
# a) tree height?
# b) elevation?
# c) soil metrics?
# d) disturbance level?
# e) fire risk index?

# Hypothesis: d and e will be more related.

#################################

# Let's visualize a few of the things we have here.

pallette <- brewer.pal(4, "Set2")

par(mfrow=c(2,2), mar=c(5,5,3,3))

hist(
  data$Elevation,
  xlab="Elevation",
  main="",
  col=pallette[1],
)

hist(
  data$Tree_Height,
  xlab="Tree height",
  main="",
  col=pallette[2]
)


hist(
  data$Disturbance_Level,
  xlab="Disturbance level",
  main="",
  col=pallette[3]
)

hist(
  data$Fire_Risk_Index,
  xlab="Fire risk index",
  main="",
  col=pallette[4]
)

# It appears that our data is more or less homogeneous.
