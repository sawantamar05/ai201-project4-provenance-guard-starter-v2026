"""Numerical boundaries and independent style measurements."""

import math
import unittest

import config
import scoring
import stylometry


class ScoringTests(unittest.TestCase):
    def test_every_score_has_one_correct_label(self):
        reached = set()
        for i in range(10001):
            value = i / 10000
            guess, label = scoring.score_to_label(value)
            expected = "human" if value <= config.HUMAN_THRESHOLD else "ai" if value >= config.AI_THRESHOLD else "unsure"
            self.assertEqual(guess, expected)
            self.assertTrue(label.strip())
            self.assertNotIn("PLACEHOLDER", label)
            reached.add(guess)
        self.assertEqual(reached, {"ai", "human", "unsure"})

    def test_threshold_boundaries_and_different_confidences(self):
        for value, expected in ((0, "human"), (config.HUMAN_THRESHOLD, "human"), (config.HUMAN_THRESHOLD+0.0001, "unsure"), (0.51, "unsure"), (config.AI_THRESHOLD-0.0001, "unsure"), (config.AI_THRESHOLD, "ai"), (0.95, "ai"), (1, "ai")):
            with self.subTest(value=value):
                self.assertEqual(scoring.score_to_label(value)[0], expected)
        self.assertNotEqual(scoring.score_to_label(0.51), scoring.score_to_label(0.95))

    def test_combination_and_disagreement_guard(self):
        self.assertAlmostEqual(scoring.combine_signals(0.8, 0.7), 0.78)
        self.assertEqual(scoring.score_to_label(scoring.combine_signals(0.95, 0.6))[0], "unsure")
        self.assertEqual(scoring.score_to_label(scoring.combine_signals(0.05, 0.8))[0], "unsure")
        for i in range(101):
            for j in range(101):
                model, style = i / 100, j / 100
                value = scoring.combine_signals(model, style)
                self.assertTrue(math.isfinite(value))
                self.assertGreaterEqual(value, 0)
                self.assertLessEqual(value, 1)
                if abs(model - style) >= 0.350000001:
                    self.assertEqual(scoring.score_to_label(value)[0], "unsure")

    def test_invalid_numerical_scores_are_rejected(self):
        for value in (-0.01, 1.01, float("nan"), float("inf"), -float("inf")):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    scoring.score_to_label(value)
                with self.assertRaises(ValueError):
                    scoring.combine_signals(value, 0.5)
                with self.assertRaises(ValueError):
                    scoring.combine_signals(0.5, value)

    def test_labels_are_cautious_and_ranges_complete(self):
        human = scoring.score_to_label(0)[1]
        unsure = scoring.score_to_label(0.5)[1]
        ai = scoring.score_to_label(1)[1]
        self.assertIn("does not verify", human)
        self.assertIn("No conclusion about the writer", unsure)
        self.assertIn("not proof", ai)
        self.assertEqual(len(scoring.label_ranges()), 3)


class StyleTests(unittest.TestCase):
    def test_word_diversity_known_examples(self):
        self.assertAlmostEqual(stylometry.type_token_ratio("Cat cat dog dog"), 0.5)
        self.assertAlmostEqual(stylometry.type_token_ratio("Alpha beta gamma"), 1)
        self.assertEqual(stylometry.type_token_ratio(""), 0)

    def test_unicode_words_and_punctuation(self):
        tokens = stylometry.words("Café déjà naïve mañana résumé")
        self.assertEqual(len(tokens), 5)
        self.assertIn("café", tokens)
        self.assertGreater(stylometry.punctuation_density("Hello—world！"), 0)
        self.assertEqual(stylometry.punctuation_density("no punctuation"), 0)
        self.assertEqual(stylometry.punctuation_density(""), 0)

    def test_sentence_spread_and_short_text_are_safe(self):
        self.assertEqual(stylometry.sentence_length_spread("One sentence only."), 0)
        self.assertEqual(stylometry.sentence_length_spread(""), 0)
        self.assertEqual(stylometry.sentence_length_spread("One two. Three four. Five six."), 0)
        self.assertGreater(stylometry.sentence_length_spread("Short. A somewhat longer sentence with seven words. Tiny."), 0)
        for text in ("", "Hello world.", "Punctuation !!!", "words only " * 4):
            with self.subTest(text=text):
                self.assertEqual(stylometry.style_signal(text), 0.5)

    def test_style_varies_with_surface_features(self):
        regular = "The system provides useful results for every user. " * 8
        varied = (
            "Stop! Beneath the rusted gate, Marisol discovered velvet scraps, a brass compass, "
            "three obsolete tickets—and, inexplicably, yesterday’s invitation. Nobody moved. "
            "Why would Joaquín leave these peculiar objects here; who expected us to understand?"
        )
        regular_score = stylometry.style_signal(regular)
        varied_score = stylometry.style_signal(varied)
        for value in (regular_score, varied_score):
            self.assertTrue(math.isfinite(value))
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 1)
        self.assertGreater(regular_score, varied_score)


if __name__ == "__main__":
    unittest.main()
