library(ggplot2)
original_titanic <- read.csv("titanic.csv")

original_titanic$pclass <- factor(original_titanic$pclass, levels = c("3", "2", "1"))

survival_class <- original_titanic %>% 
  group_by(pclass) %>% 
  summarise(stat = mean(survived))

survival_class

p <- ggplot(data = survival_class, aes(x = pclass, y = stat)) +
     geom_bar(stat = "identity", width = 0.5, color = "blue", fill = "darkblue") + 
     theme_minimal() +
     labs(x = "Class", y = "Rate of Survival (%)", title = "Survival Rate by Class")
plot <- p + coord_flip()
plot
