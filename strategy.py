import numpy as np
import re

class MarketSentimentAnalyzer:
    def analyze(self, report_text: str) -> float:
        # Mocking a Transformer-based sentiment analysis for market intelligence
        keywords = {"growth": 0.5, "innovation": 0.4, "risk": -0.3, "volatile": -0.4}
        score = 0.5
        for word, val in keywords.items():
            if word in report_text.lower(): score += val
        return np.clip(score, 0, 1)

class MonteCarloRiskAssessor:
    def simulate_p_and_l(self, initial_investment: float, iterations=1000):
        # Running a Monte Carlo simulation for deep tech investment risk
        returns = np.random.normal(0.15, 0.25, iterations)
        final_values = initial_investment * (1 + returns)
        return {"mean": np.mean(final_values), "var_95": np.percentile(final_values, 5)}

class DeepTechStrategicEngine:
    """
    Strategic Engine for technical due diligence, using NLP for sentiment
    and Monte Carlo simulations for financial risk modeling.
    """
    def __init__(self):
        self.analyzer = MarketSentimentAnalyzer()
        self.assessor = MonteCarloRiskAssessor()

    def generate_brief(self, industry_report: str, capital: float):
        sentiment = self.analyzer.analyze(industry_report)
        projections = self.assessor.simulate_p_and_l(capital)
        
        print("--- Strategic Investment Brief ---")
        print(f"Market Sentiment: {'Positive' if sentiment > 0.6 else 'Cautious'} ({sentiment:.2f})")
        print(f"Expected Value: ${projections['mean']:.2f} | Value-at-Risk (95%): ${projections['var_95']:.2f}")

if __name__ == "__main__":
    engine = DeepTechStrategicEngine()
    report = "The AI growth is massive, but market risk remains volatile due to energy constraints."
    engine.generate_brief(report, capital=1000000)
