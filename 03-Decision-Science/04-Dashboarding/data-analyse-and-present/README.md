# Analyze and Present

## 🎯 Objectives

You know the Olist data through and through by now.

It's time to analyze the data for your management, and present your results!

For this challenge, focus on creating two, three good visuals in a notebook. Once you have those, you can either present them by showing your notebook, or by copy-pasting the charts into a presentation tool of your choice.

If you want to and have enough time, you can also create a basic dashboard using Dash. That said, remember the focus of the challenge is to create an insightful chart first. Making a dashboard is a nice extra, but optional.

Remember to work together with your buddy and split the work.

## ⚙️ Setup

🚀 For this challenge you can use both:
- The `Order`, `Seller`, `Product` and `Review` classes from the `olist` module
- The original tables available in `Olist().get_data()`

We built the first classes for our Linear and Logistic Regression models. They are feature tables, but might not have all data you'd want to use in a dashboard. For example, to visualize evolutions over time, you'd have to go back to the original tables to find the purchase date, delivery date, ...

⚠️ Make sure you have the latest versions of `seller.py` and `product.py` in your `olist` module. To do so:

1. Go back to the Logistic Regression unit, and download the Recap solution.
1. Unzip the file, and inside you will find the `seller_updated.py` and `product_updated.py` files. Open those files in VS Code.
1. In your terminal navigate to the `olist` folder, and open it using VS Code.
1. Copy-paste the contents of:
   - The solution's `seller_updated.py` into your `olist/seller.py` and `olist/seller_updated.py` files.
   - The solution's `product_updated.py` into your `olist/product.py` and `olist/product_updated.py` files.

Don't hesitate to go back into some of the challenges of the previous units and dive into their **solutions** for inspiration. For example in:
- CEO Request
- Metric Design
- NPS Recap in Statistical Inference
- Delivery Time Recap in Linear Regression

## 👥 Choose a target audience

Team up with your buddy and decide:

> Who will you present to? The CEO? CFO? Head of Marketing? Sales? Investors?

Pick an audience, and think about what you want to present. If you're in doubt, scroll down to the _Need inspiration?_ section..

## 📊 Analyse the data

Start a new Jupyter Notebook for your analysis.

Import the different Olist classes we made to prepare the data. Those are a good place to get started. If you need additional information you can go back to the original `Olist().get_data()`. You'll need those if you want to plot evolutions over time. Don't make it too complicated though: today is all about presenting analysis through visualizations. So resist the urge to create even more classes. 🤓

Which brings us to this: choose 📊 the right visualization 📈 for the point you want to bring across. (Hint: don't use a pie chart...)

In a notebook, build a couple of visualizations - split the work with your buddy! Remember to keep your notebook nice and tidy! It should be runnable from top to bottom at all times...

Once you have two or three visualizations, move on to the next part! You can come back to this point once you have a first version of your dashboard running.

### Need inspiration?

Here are a couple of ideas you could implement. Don't try to do all of them today, that's impossible. Just pick a few you're interested in.

- Analyse **sales** across different dimensions:
  - Evolution over time
  - Product categories
  - Seller dimensions
  - Customer dimensions
  - By geography (customer / seller)
- Analyse **customer satisfaction** (NPS = Net Promoter Score = % promoters - % detractors, or CSAT = Customer Satisfaction = Average review score):
  - Evolution over time
  - Correlation with other variables (price, delivery time, wait time)
  - By seller (location)
  - By customer (location)
  - By product (category)
- Analyse Olist's **profitability**:
  - Evolution over time
  - Distribution across sellers
  - Distribution across product categories
  - By customer and/or seller location
- Analyse how estimated **reputation costs** impact profitability: which sellers or products have the worst impact?


### Olist's profitability?

**If (and only if)** you want to dive into profitability:

#### Revenues

**Sales fees:** Olist takes a **10% cut** on the product price (excl. freight) of each order delivered
**Subscription fees:** Olist charges **80 BRL by month** per seller

#### Costs
_Estimated_ **reputation costs** of orders with bad reviews (<= 3 stars)

💡 In the long term, bad customer experience has business implications: low repeat rate, immediate customer support cost, refunds or unfavorable word of mouth communication. We make an assumption about the monetary cost for each bad review:
```python
# review_score: cost(BRL)
{'1 star': 100
'2 stars': 50
'3 stars': 40
'4 stars': 0
'5 stars': 0}
```

## 🖥️ [Optional] Make a dashboard

Now that you have some visualizations, you can make your first dashboard.

Make an `app.py` and start creating a dashboard with Dash. Don't reinvent the wheel: start by copying from the lecture slides.

Create a first version, without any chart yet, and try to run your code:

```bash
python app.py
```

Then point your browser at `http://127.0.0.1:8050/` to see your (empty) dashboard. That's one step down! You have a basic app running.

> Pro tip: Try to get a first visualization running, and only then start adding more. The less code you have, the easier it is to debug. And once you have one visual, it's easy to start adding more.

The focus of today is on showing your first graphs. Don't go into the nitty gritty detail of getting all the margins and colors and fonts right. Hire a web developer for that!

Once you have your first version, work further with your buddy to add more visuals.

**Need inspiration?**

- Look at the same data from different angles. Try out different chart types. Which one works best?
- Look at the same data at different levels: a consolidated overview and a deep dive for the dimension of your choice.
- Try to add some interactivity: let the user choose the category they want to see.

## 🎥 Show time! Present your analysis

You have 5 minutes per buddy pair (Q&A included) to present your results.

The TAs will play the role of the CEO, CFO, Marketing Director, investor, ...

🏁 Stop your analyses 2 hours before the presentation so you have time to create your presentation (or dashboard). Once you have a basic presentation (or your dashboard running), you can still go back to add more visuals!
