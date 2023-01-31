# CodiumAI token minimization

In this repository we provide implementation for token-reduction techniques introduce in our blog ["Reduce Your Costs by 30% When Using GPT-3 for Python Code"](https://www.codium.ai/post/reduce-your-costs-by-30-when-using-gpt-3-for-python-code)

Example code for the proposed techniques is provided in `example.py`.

<p align="center">
 <table class="tg">
 <tr>
    <td class="tg-c3ow" style="background-color: white;"><h5>Tokens for baseline code</h5><img alt="Baseline Tokens" src=pics/baseline_tokens.png align="center" width="400"  style="background-color: white;"></td>
  </tr>
  <tr>
    <td class="tg-c3ow" style="background-color: white;"><h5>Tokens for tabified code</h5><img alt="Tabified Tokens" src=pics/tabified_tokens.png align="center" width="400"  style="background-color: white;"></td>
  </tr>
  <tr>
    <td class="tg-c3ow" style="background-color: white;"><h5>Tokens for tabified and minimized code</h5><img alt="Tabified and minimized code tokens" src=pics/tabified_and_minimized_tokens.png align="center" width="400"  style="background-color: white;"></td>
  </tr>
</table>
</p>

Note that both tabification and minimization operations do not change the code functionality. 

Feel free to contact if there are any questions or issues.

## Acknowledgement
To perform code minimization, we use the excellent [Python Minifier](https://github.com/dflook/python-minifier) package.
