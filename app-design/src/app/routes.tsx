import { createBrowserRouter, Navigate } from "react-router";
import { Layout } from "./components/Layout";
import { TodayPage } from "./components/pages/TodayPage";
import { CaregiversPage } from "./components/pages/CaregiversPage";
import { RoutinesPage } from "./components/pages/RoutinesPage";
import { MyBabyPage } from "./components/pages/MyBabyPage";
import { FeedingDetailPage } from "./components/pages/FeedingDetailPage";
import { HydrationDetailPage } from "./components/pages/HydrationDetailPage";
import { SleepDetailPage } from "./components/pages/SleepDetailPage";
import { DiaperDetailPage } from "./components/pages/DiaperDetailPage";
import { ActivityDetailPageV2 } from "./components/pages/ActivityDetailPageV2";
import { BathDetailPage } from "./components/pages/BathDetailPage";
import { HealthDetailPage } from "./components/pages/HealthDetailPage";
import { GrowthPage } from "./components/pages/GrowthPage";
import { MilestonesPage } from "./components/pages/MilestonesPage";
import { HealthHubPage } from "./components/pages/HealthHubPage";
import { VaccinesPage } from "./components/pages/VaccinesPage";
import { VitaminsPage } from "./components/pages/VitaminsPage";
import { HealthEventsPage } from "./components/pages/HealthEventsPage";
import { MyDataPage } from "./components/pages/MyDataPage";
import { TimelineDetailPage } from "./components/pages/TimelineDetailPage";
import { LoginPage } from "./components/pages/LoginPage";
import { OnboardingWizard } from "./components/onboarding/OnboardingWizard";
import { ProtectedRoute } from "./ProtectedRoute";

import { IntegrationsPage } from "./components/pages/IntegrationsPage";

export const router = createBrowserRouter([
  { path: "/login", Component: LoginPage },
  { path: "/onboarding", Component: OnboardingWizard },
  {
    path: "/",
    element: (
      <ProtectedRoute>
        <Layout />
      </ProtectedRoute>
    ),
    children: [
      { index: true, Component: TodayPage },
      { path: "integrations", Component: IntegrationsPage },
      { path: "caregivers", Component: CaregiversPage },
      { path: "routines", Component: RoutinesPage },
      { path: "my-baby", Component: MyBabyPage },
      { path: "my-baby/growth", Component: GrowthPage },
      { path: "my-baby/milestones", Component: MilestonesPage },
      { path: "my-baby/health", Component: HealthHubPage },
      { path: "my-baby/health/vaccines", Component: VaccinesPage },
      { path: "my-baby/health/vitamins", Component: VitaminsPage },
      { path: "my-baby/health/events", Component: HealthEventsPage },
      { path: "my-baby/data", Component: MyDataPage },
      { path: "tracker/timeline", Component: TimelineDetailPage },
      { path: "tracker/feeding", Component: FeedingDetailPage },
      { path: "tracker/hydration", Component: HydrationDetailPage },
      { path: "tracker/sleep", Component: SleepDetailPage },
      { path: "tracker/diaper", Component: DiaperDetailPage },
      { path: "tracker/activity", Component: ActivityDetailPageV2 },
      { path: "tracker/bath", Component: BathDetailPage },
      { path: "tracker/health", Component: HealthDetailPage },
    ],
  },
  { path: "*", element: <Navigate to="/" replace /> },
]);
