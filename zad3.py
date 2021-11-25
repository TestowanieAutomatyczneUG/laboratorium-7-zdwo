import math
import unittest


class Statement:
    def s(self, invoice, plays):
        total_amount = 0
        volume_credits = 0
        result = f'Statement for {invoice["customer"]}\n'

        def format_as_dollars(amount):
            return f"${amount:0,.2f}"

        for perf in invoice['performances']:
            play = plays[perf['playID']]
            if play['type'] == "tragedy":
                this_amount = 40000
                if perf['audience'] > 30:
                    this_amount += 1000 * (perf['audience'] - 30)
            elif play['type'] == "comedy":
                this_amount = 30000
                if perf['audience'] > 20:
                    this_amount += 10000 + 500 * (perf['audience'] - 20)

                this_amount += 300 * perf['audience']

            else:
                raise ValueError(f'unknown type: {play["type"]}')

            # add volume credits
            volume_credits += max(perf['audience'] - 30, 0)
            # add extra credit for every ten comedy attendees
            if "comedy" == play["type"]:
                volume_credits += math.floor(perf['audience'] / 5)
            # print line for this order
            result += f' {play["name"]}: {format_as_dollars(this_amount/100)} ({perf["audience"]} seats)\n'
            total_amount += this_amount

        result += f'Amount owed is {format_as_dollars(total_amount/100)}\n'
        result += f'You earned {volume_credits} credits\n'
        return result

class Test_statement(unittest.TestCase):
    def setUp(self):
        self.temp = Statement()
    def testInstance(self):
        self.assertIsInstance(self.temp, Statement)
    def test_pos(self):
        self.assertEqual("Statement for BigCo\n Hamlet: $650.00 (55 seats)\n As You Like It: $580.00 (35 seats)\n Othello: $500.00 (40 seats)\nAmount owed is $1,730.00\nYou earned 47 credits\n", self.temp.s({
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 55
                },
                {
                    "playID": "as-like",
                    "audience": 35
                },
                {
                    "playID": "othello",
                    "audience": 40
                }
            ]
        },
            {
                "hamlet": {"name": "Hamlet", "type": "tragedy"},
                "as-like": {"name": "As You Like It", "type": "comedy"},
                "othello": {"name": "Othello", "type": "tragedy"}
            }
        ))

    def test_pos_sth(self):
        self.assertEqual("Statement for BigCo\n sth: $740.00 (55 seats)\n As You Like It: $860.00 (70 seats)\n Othello: $400.00 (5 seats)\nAmount owed is $2,000.00\nYou earned 90 credits\n", self.temp.s({
            "customer": "BigCo",
            "performances": [
                {
                  "playID": "sth",
                  "audience": 55
                },
                {
                  "playID": "as-like",
                  "audience": 70
                },
                {
                  "playID": "othello",
                  "audience": 5
                }
            ]
        },
            {
                "sth": {"name": "sth", "type": "comedy"},
                "as-like": {"name": "As You Like It", "type": "comedy"},
                "othello": {"name": "Othello", "type": "tragedy"}
            }
        ))

    def test_pos_a(self):
        self.assertEqual("Statement for A\n a: $306.00 (2 seats)\n As You Like It: $860.00 (70 seats)\nAmount owed is $1,166.00\nYou earned 54 credits\n", self.temp.s({
            "customer": "A",
            "performances": [
                {
                  "playID": "a",
                  "audience": 2
                },
                {
                  "playID": "as-like",
                  "audience": 70
                }
            ]
        },
            {
                "a": {"name": "a", "type": "comedy"},
                "as-like": {"name": "As You Like It", "type": "comedy"},
                "othello": {"name": "Othello", "type": "tragedy"}
            }
        ))

    def test_pos_one(self):
        self.assertEqual("Statement for A\n a: $8,300.00 (1000 seats)\nAmount owed is $8,300.00\nYou earned 1170 credits\n", self.temp.s({
            "customer": "A",
            "performances": [
                {
                  "playID": "a",
                  "audience": 1000
                }
            ]
        },
            {
                "a": {"name": "a", "type": "comedy"}
            }
        ))

    def test_exc_type(self):
        self.assertRaises(ValueError, self.temp.s, {
            "customer": "A",
            "performances": [
                {
                    "playID": "a",
                    "audience": 1000
                }
            ]
        }, {
            "a": {"name": "a", "type": "drama"}
        })

    def test_exc_tup(self):
        self.assertRaises(ValueError, self.temp.s, {
            "customer": "A",
            "performances": [
                {
                    "playID": "a",
                    "audience": 1000
                }
            ]
        }, {
                "a": {"name": "a", "type": ()}
        })
    def test_exc_arr(self):
        self.assertRaises(ValueError, self.temp.s, {
            "customer": "A",
            "performances": [
                {
                    "playID": "a",
                    "audience": 1000
                }
            ]
        }, {
            "a": {"name": "a", "type": []}
        })
    def test_exc_int(self):
        self.assertRaises(ValueError, self.temp.s, {
            "customer": "A",
            "performances": [
                {
                    "playID": "a",
                    "audience": 1000
                }
            ]
        }, {
            "a": {"name": "a", "type": 1}
        })

    def test_exc_dict(self):
        self.assertRaises(ValueError, self.temp.s, {
            "customer": "A",
            "performances": [
                {
                    "playID": "a",
                    "audience": 1000
                }
            ]
        }, {
            "a": {"name": "a", "type": {}}
        })

    def tearDown(self):
        self.temp = None

if __name__ == '__main__':
    unittest.main()