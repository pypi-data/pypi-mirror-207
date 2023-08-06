import re

from spacy.language import Language
from spacy.tokens import Doc, Span

from .logs import get_logger

logger = get_logger(__name__)


@Language.factory(
    "sentex",
    default_config={
        "sentence_regex": "",
        "ignore_regex": "",
        "annotate_ents": False,
        "label": "Sentex",
    },
)
def create_sentex_component(
    nlp: Language,
    name: str,
    sentence_regex: str,
    ignore_regex: str,
    annotate_ents: bool,
    label: str,
):
    return Sentex(nlp, sentence_regex, ignore_regex, annotate_ents, label)


class Sentex:
    """
    Sentex is a spaCy pipeline component that adds spans to the list `Doc._.sentex`
    based on regular expression matches within each sentence of the document. If an
    `ignore_regex` is given, sentences matching that regular expression will be ignored.

    nlp: `Language`,
        A required argument for spacy to use this as a factory
    sentence_regex : `str`,
        A regular expression to match spans within each sentence of the document.
    ignore_regex : `str`,
        A regular expression to identify sentences that should be ignored.
    annotate_ents: `bool`,
        Write/overwrite matches to Doc.ents
    label: `str`,
        If annotate_ents == True, the label for the matched entity
    """

    def __init__(
        self,
        nlp: Language,
        sentence_regex: str,
        ignore_regex: str,
        annotate_ents: bool,
        label: str,
    ):
        self.sentence_regex = sentence_regex
        self.ignore_regex = ignore_regex
        self.annotate_ents = annotate_ents
        self.label = label

        if not Doc.has_extension("sentex"):
            Doc.set_extension("sentex", default=[])

    def __call__(self, doc: Doc) -> Doc:
        # keep track of previous sentence
        prev_sent = None
        for i, sent in enumerate(doc.sents):
            logger.debug(f"sentence {i}: {sent}")
            should_ignore = self.ignore_regex.strip() != "" and bool(
                re.search(self.ignore_regex, sent.text)
            )
            if should_ignore:
                logger.debug("sentence ignored")
                prev_sent = sent
                continue
            for match in re.finditer(self.sentence_regex, sent.text):
                logger.debug(f"match: {str(match)}")
                start, end = match.span()
                # convert to doc in order to use 'expand' alignment mode
                # in case indicies are inside token boundaries
                span = sent.as_doc().char_span(start, end, alignment_mode="expand")
                if span is not None:
                    # realign span so start/end are relative to doc, not sent
                    span = self._realign_span(doc, span, prev_sent)
                    logger.debug(f"match {span.text} start: {start} end: {end}")
                    logger.debug(
                        f"start {span.start} end {span.end}\
                        start char {span.start_char} end char {span.end_char}"
                    )
                    logger.debug("adding match to sentex")
                    doc._.sentex.append(span)
                else:
                    logger.debug("span is None")
            prev_sent = sent
        if self.annotate_ents:
            self.set_annotations(doc)
        return doc

    def set_annotations(self, doc):
        """Modify the document in place.
        Logic taken from spacy.pipeline.entityruler.EntityRuler
        """
        entities = list(doc.ents)
        logger.debug(f"current entities: {entities}")
        new_entities = []
        seen_tokens = set()
        matches = self._get_matches(doc)
        for match_id, start, end in matches:
            # check for end - 1 here because boundaries are inclusive
            if start not in seen_tokens and end - 1 not in seen_tokens:
                span = Span(doc, start, end, label=match_id)
                new_entities.append(span)
                logger.debug(f"new entity: {span.text} start: {start} end: {end}")
                entities = [
                    e for e in entities if not (e.start < end and e.end > start)
                ]

                seen_tokens.update(range(start, end))
        doc.ents = entities + new_entities

    def _get_matches(self, doc: Doc):
        return [(self.label, m.start, m.end) for m in doc._.sentex]

    def _realign_span(self, doc: Doc, span: Span, prev_sent: Span):
        offset = 0 if prev_sent is None else prev_sent.end
        start = span.start + offset
        end = span.end + offset
        return doc[start:end]
    
@Language.factory(
    "size",
    default_config={
        "size_regex": r"(i?)((\d+(\.\d+)?)\s*([Xx]\s*(\d+(\.\d+)?)\s*([Xx]\s*(\d+(\.\d+)?))?)?\s*)(?=\W?[cm]m)",
        "sentex_only": True,
        "annotate_ents": True,
        "label": "SIZE"
    },
)
def create_size_component(
    nlp: Language,
    name: str,
    size_regex: str,
    sentex_only: bool,
    annotate_ents: bool,
    label: str
):
    return Size(nlp, size_regex, sentex_only, annotate_ents, label)


class Size:
    """
    Size is a spaCy pipeline component that adds spans to the list `Doc._.size`
    based on regular expression matches within each sentence of the document. 

    nlp: `Language`,
        A required argument for spacy to use this as a factory
    size_regex : `str`,
        A regular expression to match spans within each sentence of the document.
    sentex_only : `bool`,
        Only match in sentences with Sentex-matched entities
    annotate_ents: `bool`,
        Write/overwrite matches to Doc.ents
    label: `str`,
        If annotate_ents == True, the label for the matched entity
    """

    def __init__(
        self,
        nlp: Language,
        size_regex: str,
        sentex_only: bool,
        annotate_ents: bool,
        label: str
    ):
        self.size_regex = size_regex
        self.sentex_only = sentex_only
        self.annotate_ents = annotate_ents
        self.label = label

        if not Doc.has_extension("size"):
            Doc.set_extension("size", default=[])

    def __call__(self, doc: Doc) -> Doc:
        self.process(doc)
        if self.annotate_ents:
            self.set_annotations(doc)
        return doc
    
    def set_annotations(self, doc):
        """Modify the document in place.
        Logic taken from spacy.pipeline.entityruler.EntityRuler
        """
        entities = list(doc.ents)
        logger.debug(f"current entities: {entities}")
        new_entities = []
        seen_tokens = set()
        matches = self._get_matches(doc)
        for match_id, start, end in matches:
            # check for end - 1 here because boundaries are inclusive
            if start not in seen_tokens and end - 1 not in seen_tokens:
                span = Span(doc, start, end, label=match_id)
                new_entities.append(span)
                logger.debug(f"new entity: {span.text} start: {start} end: {end}")
                entities = [
                    e for e in entities if not (e.start < end and e.end > start)
                ]

                seen_tokens.update(range(start, end))
        doc.ents = entities + new_entities
    
    def process(self, doc: Doc) -> Doc:
        if self.sentex_only:
            sents = set([span.sent for span in doc._.sentex])
        else:
            sents = doc.sents
        for sent in sents:
            match = re.search(self.size_regex, str(sent))
            if match is None:
                continue
            start, end = match.span()
            num_start = sent.start_char + start
            num_end = sent.start_char + end

            span = sent.doc.char_span(num_start,num_end, alignment_mode='contract')
            logger.debug(f'span: {span} indexes: {num_start} to {num_end}')
            size = self.parse_size(str(span))
            doc._.size.append((span, size))

    def _get_matches(self, doc: Doc):
        return [(self.label, m[0].start, m[0].end) for m in doc._.size]
    
    def parse_size(self, text: str) -> float:
        sizes = [n for n in text.lower().replace('x',' ').split(' ') if n != '']
        sizes = [float(n) for n in sizes]
        sizes = sizes if len(sizes) <= 2 else sizes[:2]
        size = max(sizes)
        return size
