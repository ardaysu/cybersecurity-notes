import unittest
from detection import detect


def event(i, time, user, result='failure', ip='198.51.100.24'):
    return dict(id=str(i), time=time, user=user, result=result, src_ip=ip,
                source='identity', event='login', session_id='S' if result == 'success' else '')


class DetectionTests(unittest.TestCase):
    def test_window_crosses_fixed_boundary(self):
        rows = [event(i, '09:04:00' if i < 3 else '09:06:00', str(i)) for i in range(6)]
        self.assertEqual(detect(rows)[0]['targeted_users'], 6)

    def test_many_attempts_one_user_do_not_meet_distinct_threshold(self):
        self.assertEqual(detect([event(i, '09:02:00', 'deniz') for i in range(50)]), [])

    def test_success_requires_source_target_and_order(self):
        rows = [event(i, '09:02:00', str(i)) for i in range(5)]
        rows += [event(10, '09:03:00', '1', 'success'),
                 event(11, '09:03:00', 'other', 'success'),
                 event(12, '09:03:00', '1', 'success', '203.0.113.10'),
                 event(13, '09:01:00', '1', 'success'),
                 event(14, '09:08:00', '1', 'success')]
        self.assertEqual([r['event_id'] for r in detect(rows)[0]['success_matches']], ['10'])

    def test_left_window_boundary_is_excluded(self):
        rows = [event(0, '09:00:00', '0')]
        rows += [event(i, '09:05:00', str(i)) for i in range(1, 5)]
        self.assertEqual(detect(rows), [])


if __name__ == '__main__':
    unittest.main()
