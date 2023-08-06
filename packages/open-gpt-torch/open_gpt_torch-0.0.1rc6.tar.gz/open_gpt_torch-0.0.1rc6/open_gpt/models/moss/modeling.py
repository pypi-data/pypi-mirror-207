from typing import Optional

from open_gpt.models.modeling import BaseModel


class MossModel(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load_model_and_transforms(
        self, model_name_or_path: str, tokenizer_name_or_path: Optional[str] = None
    ):
        from ..loading import load_model_and_tokenizer

        self.model, self.tokenizer = load_model_and_tokenizer(
            model_name_or_path,
            tokenizer_name_or_path=tokenizer_name_or_path,
            dtype=self._dtype,
            device=self._device,
            device_map=self._device_map,
            no_split_module_classes=["MossBlock"],
        )

        self.model.eval()

        if self.tokenizer.pad_token_id is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
            self.tokenizer.pad_token_id = self.tokenizer.eos_token_id
        self.tokenizer.padding_side = "left"
