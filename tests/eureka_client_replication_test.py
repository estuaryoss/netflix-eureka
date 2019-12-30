#!/usr/bin/env python3
import time
import unittest
from urllib.error import URLError

from tests.client.eureka_client import EurekaClient
from tests.utils.docker_utils import DockerUtils


class FlaskServerTestCase(unittest.TestCase):
    file = "docker-compose.yml"
    time_to_wait_until_compose_up = 60
    time_to_wait_until_discovery_up = 5

    def setUp(self):
        DockerUtils.down(file=self.file)

    def test_eureka_replication_both_up(self):
        DockerUtils.up_service(self.file, "eureka-server1")
        DockerUtils.up_service(self.file, "eureka-server2")
        time.sleep(self.time_to_wait_until_compose_up)
        DockerUtils.up_service(self.file, "estuary-discovery")
        time.sleep(self.time_to_wait_until_discovery_up)
        apps_list1 = EurekaClient("http://localhost:8080/eureka/v2").get_apps()
        apps_list2 = EurekaClient("http://localhost:8081/eureka/v2").get_apps()
        self.assertEqual(len(apps_list1), 1)
        self.assertEqual(apps_list1, apps_list2)

    def test_eureka_replication_second_recovers(self):
        DockerUtils.up_service(self.file, "eureka-server1")
        DockerUtils.up_service(self.file, "eureka-server2")
        time.sleep(self.time_to_wait_until_compose_up)
        DockerUtils.up_service(self.file, "estuary-discovery")
        time.sleep(self.time_to_wait_until_discovery_up)
        DockerUtils.stop_service(self.file, "eureka-server2")
        apps_list1 = EurekaClient("http://localhost:8080/eureka/v2").get_apps()
        self.assertEqual(len(apps_list1), 1)
        try:
            EurekaClient("http://localhost:8081/eureka/v2").get_apps()
        except Exception as e:
            self.assertIsInstance(e, URLError)
        DockerUtils.start_service(self.file, "eureka-server2")
        time.sleep(self.time_to_wait_until_compose_up)
        apps_list1 = EurekaClient("http://localhost:8080/eureka/v2").get_apps()
        apps_list2 = EurekaClient("http://localhost:8081/eureka/v2").get_apps()
        self.assertEqual(len(apps_list1), 1)
        self.assertEqual(apps_list1, apps_list2)

    def test_eureka_replication_first_recovers(self):
        DockerUtils.up_service(self.file, "eureka-server1")
        DockerUtils.up_service(self.file, "eureka-server2")
        time.sleep(self.time_to_wait_until_compose_up)
        DockerUtils.up_service(self.file, "estuary-discovery")
        time.sleep(self.time_to_wait_until_discovery_up)
        DockerUtils.stop_service(self.file, "eureka-server1")
        apps_list2 = EurekaClient("http://localhost:8081/eureka/v2").get_apps()
        self.assertEqual(len(apps_list2), 1)
        try:
            EurekaClient("http://localhost:8080/eureka/v2").get_apps()
        except Exception as e:
            self.assertIsInstance(e, URLError)
        DockerUtils.start_service(self.file, "eureka-server1")
        time.sleep(self.time_to_wait_until_compose_up)
        apps_list1 = EurekaClient("http://localhost:8080/eureka/v2").get_apps()
        apps_list2 = EurekaClient("http://localhost:8081/eureka/v2").get_apps()
        self.assertEqual(len(apps_list2), 1)
        self.assertEqual(apps_list1, apps_list2)

    def test_eureka_replication_just_one_up_and_recovers(self):
        DockerUtils.up_service(self.file, "eureka-server1")
        time.sleep(self.time_to_wait_until_compose_up)
        DockerUtils.up_service(self.file, "estuary-discovery")
        time.sleep(self.time_to_wait_until_discovery_up)
        apps_list1 = EurekaClient("http://localhost:8080/eureka/v2").get_apps()
        self.assertEqual(len(apps_list1), 1)
        try:
            EurekaClient("http://localhost:8081/eureka/v2").get_apps()
        except Exception as e:
            self.assertIsInstance(e, URLError)

        DockerUtils.stop_service(self.file, "eureka-server1")
        time.sleep(self.time_to_wait_until_compose_up)
        DockerUtils.up_service(self.file, "eureka-server1")
        time.sleep(self.time_to_wait_until_compose_up)
        apps_list1 = EurekaClient("http://localhost:8080/eureka/v2").get_apps()
        self.assertEqual(len(apps_list1), 1)


if __name__ == '__main__':
    unittest.main()
