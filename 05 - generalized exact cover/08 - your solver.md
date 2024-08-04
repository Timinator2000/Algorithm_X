# Extending your AlgorithmXSolver Subclass

Adding optional requirements to your solver is as easy passing a third argument to the AlgorithmXSolver constructor. Before I walk through the code, I need to address an alternate option that allows Algorithm X to handle a generalized exact cover. In the [Wikipedia Exact Cover]( https://en.wikipedia.org/wiki/Exact_cover) discussion, you will see the following:

>As Knuth explains, a generalized exact cover problem can be converted to an equivalent exact cover problem by simply appending one row for each secondary column, containing a single 1 in that column.[6] If in a particular candidate solution a particular secondary column is satisfied, then the added row isn't needed. But if the secondary column isn't satisfied, as is allowed in the generalized problem but not the standard problem, then the added row can be selected to ensure the column is satisfied.

The next paragraph in the Wikipedia article goes on to explain:

>But Knuth goes on to explain that it is better working with the generalized problem directly, because the generalized algorithm is simpler and faster: __A simple change to his Algorithm X allows secondary columns to be handled directly.__ [emphasis added]

__With my AlgorithmXSolver, you never need to add extra rows as is suggested in the first paragraph. Coud you? Yes, you could. You could add the extra rows and only use the requirements argument. You could do some of both. However, I don’t recommend any of that. Conceptually, problems have requirements (primary constraints) and optional requirements (secondary constraints). I recommend always keeping them separate, passing them to the AlgorithmXSolver constructor separately, and letting the AlgorithmXSolver handle the needed algorithmic changes.__

