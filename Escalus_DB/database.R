library('dplyr')

DB <- read.csv("jb.txt")

names(DB)

#list <- select(DB, Judge.Identification.Number, Judge.First.Name, Judge.Last.Name, Birth.year, Place.of.Birth..City., Place.of.Birth..State., Court.Name, Court.Type, President.name, Party.Affiliation.of.President, Renominating.President.name, Party.Affiliation.of.Renominating.President)

# Relevant Features
features <- as.character(read.csv("features.csv", header=F)$V1)
features[1][1] <- 'Judge.Identification.Number'

judges <- select(DB, one_of(features))
judges <- arrange(judges, Name.of.School)

head(judges)


school_names <- as.factor(judges$Name.of.School)
levels(school_names) <- 1:length(levels(school_names))
school_nums <- as.numeric(levels(school_names))