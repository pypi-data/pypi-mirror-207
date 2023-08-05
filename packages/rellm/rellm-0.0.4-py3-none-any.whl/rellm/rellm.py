from concurrent.futures import ThreadPoolExecutor
from typing import Dict, Set

import numpy as np
import regex
from transformers import LogitsProcessor, PreTrainedModel, PreTrainedTokenizer


class CustomLogitsMask(LogitsProcessor):
    """
    CustomLogitsMask is a LogitsProcessor that masks logits for tokens that are 
    not in the allowed token ids set.
    """
    def __init__(self, allowed_token_ids):
        self.allowed_token_ids = set(allowed_token_ids)

    def __call__(self, input_ids, scores):
        mask = np.ones_like(scores) * -1e10
        for token_id in self.allowed_token_ids:
            mask[:, token_id] = 0
        scores = scores + mask 
        return scores

def complete_re(prompt:str, pattern: regex.Pattern, tokenizer: PreTrainedTokenizer, 
                model: PreTrainedModel, max_new_tokens: int = 3, 
                stop_after_match: bool = True,
                debug: bool = False,
                **model_kwargs):
    """
    Complete a prompt with a regex pattern.
    """
    gen_tokens = 0
    partial_completion = ""
    prompt_plus_completion = prompt + partial_completion

    token_validator = TokenValidator(tokenizer)

    while gen_tokens < max_new_tokens:
        prompt_token_ids = tokenizer.encode(prompt_plus_completion, return_tensors="pt")
        prompt_length = prompt_token_ids.shape[1]

        allowed_token_ids = token_validator.get_valid_next_tokens(partial_completion, pattern)
        custom_mask_processor = CustomLogitsMask(allowed_token_ids)

        output_ids = model.generate(prompt_token_ids,
                                    max_new_tokens=1,
                                    pad_token_id=tokenizer.eos_token_id,
                                    logits_processor=[custom_mask_processor],
                                    **model_kwargs
        )
        new_token_ids = output_ids[0, prompt_length:]
        output_text = tokenizer.decode(new_token_ids, skip_special_tokens=True)
        partial_completion += output_text
        prompt_plus_completion = prompt_plus_completion + output_text
        if debug:
            print("step={} completion={}".format(gen_tokens, partial_completion))

        if stop_after_match and pattern.match(partial_completion):
            break
        gen_tokens += 1

    return partial_completion

class TokenValidator:
    def __init__(self, tokenizer: PreTrainedTokenizer):
        self.tokenizer = tokenizer
        self.decoded_tokens_cache = self.build_decoded_tokens_cache(tokenizer)

    @staticmethod
    def build_decoded_tokens_cache(tokenizer: PreTrainedTokenizer) -> Dict[int, str]:
        return {token_id: tokenizer.decode(token_id) for _, token_id in tokenizer.get_vocab().items()}

    def is_valid_token(self, token_id: int, partial_completion: str, pattern: regex.Pattern) -> bool:
        decoded_token = self.decoded_tokens_cache[token_id]
        return pattern.match(partial_completion + decoded_token, partial=True)

    def get_valid_next_tokens(self, partial_completion: str, pattern: regex.Pattern) -> Set[int]:
        with ThreadPoolExecutor():
            valid_token_ids = set(
                filter(
                    lambda token_id: self.is_valid_token(token_id, partial_completion, pattern),
                    self.decoded_tokens_cache.keys()
                )
            )

        return valid_token_ids