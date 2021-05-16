## Study Material
- [Introduction to Bayesian Thinking *by Clyde et. al.*](https://statswithr.github.io/book/)

## Concept Map
- Bayes Rule & Basic Conditional Probability
  - Completely Understand P( *HIV positive* | *positive test*) example
  - Keep reviewing this, do not overlook
- Bayesian vs Frequentist approach to estimating a parameter


## Notes

date: 01/03/2021<br>

- How to think about Bayesian Inference using Bayes' rule?
  - Bayes' rule allows us to **update** our estimate of the probability of an event based on certain observations.
  - We have some *prior* knowledge of a thing.
  - Now we collect information about the thing and allow that new information to update our *prior* thereby giving us the *posterior*.


- How is the Bayesian approach different from the Frequentist approach of probability?
  - Frequentist approach is more absolute. Wanna estimate probability of success? conduct 1000 trials and count the number of successes. P(succ) = n(succ)/1000
  - Bayesian approach allows us the freedom of having *any a priori* belief about P(succ) as long as it is mathematically consistent. Then we can gather more data and improve our estimate
  - Frequentist estimates of confidence intervals are harder to interpret. 95% confidence interval DOES NOT mean 95% chance of finding the true value within the interval range
  - Per Bayesian approach, a credible confidence interval is proposed that DOES allow the statistician to say true value is contained in the credible interval with a 95% chance

date: 01/04/2021

How does this translate to differences in making inferences about a population?
- In frequentist approach it is pretty simple, make a null hypothesis and using the data find the probability of observing value as extreme as the data. If that value, p-value is too low then we reject H<sub>0</sub>, i.e. if the probability of randomly observing the data under H<sub>0</sub> is too low then H<sub>0</sub> must be false
  - It can be argued that the above approach is unsatisfactory to make direct statements about the probability of our hypothesis being true or false
- In Bayesian approach, we can assume any prior belief about the model (analogous to the null hypothesis), where the model is used to explain a population/data. Next we observe the data and ask ourselves, "how likely is it to observe this data if the prior is true?" i.e. we compute the likelihood of observing the data for a given prior under the assumption that the prior is true. Next we use the Bayes' rule to *update* our prior based on the likelihood we just computed. The updates prior is the posterior and then it is simply a matter of selecting the model with the highest posterior probability.
  - In short,
    - Assume prior probability of model being true
    - Compute likelihood of observing data if model is true
    - compute posterior probability of model being true given the observation of data
  - Notice how in Bayesian approach, instead of finding the p-value, we update the prior. This enables us to update our beliefs to be more and more accurate as we see new data. It also enables us to directly select the model with the larger posterior instead of having to rely on an arbitrary confidence limit of p-value to make a decision for us
  - This does not mean that there are no dangers in this way of thinking
    - if the prior is too far from the truth or we do not have enough data, then the prior might dominate the likelihood and not update enough to give us the correct conclusion

Up Next: Bayesian Inference
