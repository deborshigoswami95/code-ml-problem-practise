# Read 1 Paper a day for 100 days

## Table

|Date|Paper Title|Link|Completed|Notes|
|----|-----------|----|---------|-----|
|2024-11-02|[What Are the Odds? Language Models Are Capable of Probabilistic Reasoning](#what-are-the-odds?-language-models-are-capable-of-probabilistic-reasoning)|https://arxiv.org/pdf/2406.12830|Yes||
|2024-11-03|Personalized Audiobook Recommendations at Spotify Through Graph Neural Networks|https://arxiv.org/pdf/2403.05185|||
|2024-11-04|Sampling-Bias-Corrected Neural Modeling for Large Corpus Item Recommendations|https://storage.googleapis.com/gweb-research2023-media/pubtools/5716.pdf|||


## Summaries
-----------------------

### What Are the Odds? Language Models Are Capable of Probabilistic Reasoning

**Key Idea**<br>
LLMs can make statistical inferences ( like estimating percentiles, or probability of observed data ) given some basic context about a distribution to varied extents based on the distribution, task, context & shot-examples.

**Summary**<br>
- The paper is largely an experiment done on popular LLMs - GPT 3.5 Turbo, GPT 4 Turbo, Gemini 1.0 Ultra
- Three types of tasks
  - Estimating a percentile: *Return the percentile of the value {X} within a normal distribution with mean {Y} and standard deviation {Z}.*
  - Sampling data: *Sample a number from the normal distribution with mean {X} and standard deviation {Y}.*
  - Calculating Probabilities: *Calculate the probability that a value falls between {W} and {X} in a normal distribution with mean {Y} and standard dev. {Z}.*
- Key Results
  - Different tasks have different performances. Order of performance: Percentile task > Probability task > Sampling task
  - Percentile estimation task especially has impressive results especially for Uniform Distribution & Normal distribution 
  - Sampling task has worst performance but the results are still interesting. See uniform & normal distribution sampling. Pretty clear bias to the mean and interesting biases slightly off center
  - For real world distributions, more context about the distribution improves performance
  - Few shot examples improve performance
  - Within distribution examples do better than same family distribution examples
  - Percentiles & percentages regularly underestimate the presence of extreme points



**Discussion**
  - The paper does a good job discussing results but authors shy away from analysis of what these results imply for LLM and their inner workings.
  - The sampling task having some pretty intense biases points towards the LLM regressing towards the mean. This may be a consequence of the token sampling algo's ( like beam search ) which favor high probbility, unsurprising tokens.
  - This has been an issue with LLMs for a while. The authors could investigated things like widening the beam or other sampling strategies.
  - For the sampling task, I wonder if adding previous sample history might change predictions in any way. What does that say about sampling as a "reasoning task"?
  - Humans are very very bad at sampling, just ask someone to pick a number between 0 & 9. There will be clear biases when repeated across many participants. Reasoning and sampling are not the same things.




